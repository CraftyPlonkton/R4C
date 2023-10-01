from django.contrib import admin
from django.urls import path

from orders.views import week_report
from robots.views import robot_create

urlpatterns = [
    path('robot-create/', robot_create, name='robot_create'),
    path('week-report/', week_report, name='week_report'),
    path('admin/', admin.site.urls),
]
