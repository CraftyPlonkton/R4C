from django.core import mail
from django.test import TestCase

from customers.models import Customer
from orders.models import Order
from robots.models import Robot


class NotificationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.customer_1 = Customer.objects.create(email='customer_1@mail.com')
        cls.customer_2 = Customer.objects.create(email='customer_2@mail.com')
        cls.first_order = Order.objects.create(
            id=1, customer=cls.customer_1, robot_serial='R2-D2')
        cls.second_order = Order.objects.create(
            id=2, customer=cls.customer_2, robot_serial='R2-D2')

    def test_email_notification(self):
        Robot.objects.create(
            serial='R2-D2',
            model='R2',
            version='D2',
            created='2022-12-31 23:59:59'
        )
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.to, [self.customer_1.email])
        self.assertFalse(Order.objects.filter(id=1).exists())
