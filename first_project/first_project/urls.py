from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import todoapp
import users
from todoapp.views import ProjectViewSet, ToDoViewSet, ProjectAPIView, ToDoAPIView
from users.views import UserViewSet, UserAPIView

router = DefaultRouter()
router.register('users', UserViewSet, basename=users)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', UserViewSet.as_view({'get': 'list'})),
    path('api/users/<int:pk>/', UserAPIView.as_view()),
    path('api/project/', ProjectViewSet.as_view({'get': 'list'})),
    path('api/project/<int:pk>/', ProjectAPIView.as_view()),
    path('api/todo/', ToDoViewSet.as_view({'get': 'list'})),
    path('api/todo/<int:pk>/', ToDoAPIView.as_view()),

]
