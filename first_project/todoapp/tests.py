from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from mixer.backend.django import mixer

from todoapp.models import ToDo
from todoapp.views import ProjectModelViewSet
from users.models import CustomUser
from users.views import UserModelViewSet


class TestUsersView(TestCase):

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser(email='test@test.ru', password='123')

    def test_get_list_user(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.admin)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectView(APITestCase):

    def setUp(self) -> None:
        self.admin = CustomUser.objects.create_superuser(email='test@test.ru', password='123')

    def test_get_list(self):
        factory = APIRequestFactory()

        request = factory.post('/api/project/', {
            "id": 1,
            "name": "First",
            "repo_link": "http://www.ru",
            "users": [
                1
            ]
         })
        force_authenticate(request, user=self.admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_client_todo(self):
        todo = mixer.blend(ToDo)
        self.client.login(username='test@test.ru', password='123')
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
