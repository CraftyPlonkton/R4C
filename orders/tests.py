import re
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class WeekReportTest(TestCase):
    def test_xlsx_file_response(self):
        url = reverse('week_report')
        response = self.client.get(url)
        attach, file_name = response.get('Content-Disposition').split('; ')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(attach, 'attachment')
        self.assertTrue(re.search(r'week_report-.+\.xlsx', file_name))
