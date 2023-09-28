from django.contrib import admin
from django.urls import path

from robots.views import robot_create

urlpatterns = [
    path('robot-create/', robot_create, name='robot_create'),
    path('admin/', admin.site.urls),
]
