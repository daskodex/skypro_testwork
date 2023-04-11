from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from .models import SimplePerson
from .serializers import SimplePersonSerializer

from rest_framework import status
from rest_framework.request import Request, WrappedAttributeError
from rest_framework.test import APIClient, APIRequestFactory, RequestsClient, APITestCase

factory = APIRequestFactory()


class TestInitializer(TestCase):

    def test_request_type(self):
        request = Request(factory.get('/'))

        message = (
            'The `request` argument must be an instance of '
            '`django.http.HttpRequest`, not `rest_framework.request.Request`.'
        )
        with self.assertRaisesMessage(AssertionError, message):
            Request(request)


class TestGetPatchMethod(APITestCase):
    """ Оснавная группа тестов, проверяюся PATCH и GET запросы"""

    def setUp(self):
        self.url_endpoint = '/resume/'
        self.url_exist = '/resume/1/'
        self.url_not_exist = '/resume/50/'
        self.my_model_1 = SimplePerson.objects.create(name='name_1', status='status_2')
        self.my_model_2 = SimplePerson.objects.create(name='name_2', status='status_2')

        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_get_my_model_list(self):
        response = self.client.get(self.url_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        expected_data = SimplePersonSerializer([self.my_model_1, self.my_model_2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_get_resume_method(self):
        response = self.client.get(self.url_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_resume_method_single(self):
        response = self.client.get(self.url_exist)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_resume_method_single(self):
        response = self.client.get(self.url_not_exist)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_resume_method_without_auth(self):
        self.client.logout()
        response = self.client.patch(self.url_exist)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_resume_method_with_auth(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'name': 'name_1'}
        response = self.client.patch(self.url_exist, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)