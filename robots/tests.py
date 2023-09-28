from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from robots.models import Robot


class RobotCreateTest(TestCase):
    def test_robot_create(self):
        url = reverse('robot_create')
        count = Robot.objects.count()
        initial_data = {
            'model': 'r2',
            'version': 'e4',
            'created': '2022-12-31 23:59:59'
        }
        expected_data = {
            'model': 'R2',
            'version': 'E4',
            'serial': 'R2-E4',
            'created': '2022-12-31T23:59:59Z'
        }
        response = self.client.post(
            url, initial_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(Robot.objects.count(), count + 1)
        response_data = response.json()
        self.assertEqual(response_data, expected_data)
