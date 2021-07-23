from django.test import TestCase

from .models import Requests, TypeRequest


class RequestTestCases(TestCase):
    def setUp(self) -> None:
        self.type = TypeRequest.objects.create(type='remont')
        Requests.objects.create(
            name='Anton',
            type=self.type,
            request='Сломался пылесос',
            email='1234@mail.ru',
        )

    def test_add_request(self):
        """Тестируем наличие дублирования"""
        self.assertEqual(Requests.objects.count(),1)