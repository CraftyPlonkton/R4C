from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from orders.models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def send_availability_notify(sender, instance, created, **kwargs):
    """Отправка имейл оповещения покупателю о появлении нужного робота,
    по самому раннему заказу и удаление заказа из списка ожидания."""
    order = Order.objects.filter(
        robot_serial=instance.serial
    ).select_related(
        'customer'
    ).first() if created else None
    if order:
        html_message = render_to_string(
            'availability_notify.html', {'robot': instance}
        )
        send_mail(
            'Робот в наличии',
            '',
            None,
            [order.customer.email],
            fail_silently=True,
            html_message=html_message
        )
        order.delete()
