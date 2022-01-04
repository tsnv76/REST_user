from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from django.contrib.auth.models import User

from users.models import CustomUser
from users.views import UserModelViewSet


class TestProjectView(TestCase):

    def test_get_list(self):
        admin = CustomUser.objects.create_superuser(email='test@test.ru', password='123')
        factory = APIRequestFactory()
        request = factory.post('/api/project/', {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birthday_year': 1799
        })
        force_authenticate(request, user=admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['last_name'], 'Пушкин')
        request = factory.get('/api/authors/')
        force_authenticate(request, user=admin)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
