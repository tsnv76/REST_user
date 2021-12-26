from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import todoapp
import users
from todoapp.views import ProjectViewSet, ToDoViewSet, ProjectAPIView, ToDoAPIView, UpdateProjectAPIView, \
    UpdateTodoAPIView, CreateProjectAPIView, DeleteProjectAPIView, CreateTodoAPIView, DeleteTodoAPIView, \
    ProjectParamFilterViewSet, TodoParamFilterViewSet
from users.views import UserViewSet, UserAPIView, UpdateUserAPIView

router = DefaultRouter()
router.register('users', UserViewSet, basename=users)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)
router.register('project_filters', ProjectParamFilterViewSet)
router.register('todo_filters', TodoParamFilterViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', UserViewSet.as_view({'get': 'list'})),
    path('api/users/<int:pk>/', UserAPIView.as_view()),
    path('api/users/update/<int:pk>/', UpdateUserAPIView.as_view()),
    path('api/project/', ProjectViewSet.as_view({'get': 'list'})),
    path('api/project/<int:pk>/', ProjectAPIView.as_view()),
    path('api/project/update/<int:pk>/', UpdateProjectAPIView.as_view()),
    path('api/project/create/', CreateProjectAPIView.as_view()),
    path('api/project/delete/<int:pk>/', DeleteProjectAPIView.as_view()),
    path('api/todo/', ToDoViewSet.as_view({'get': 'list'})),
    path('api/todo/<int:pk>/', ToDoAPIView.as_view()),
    path('api/todo/update/<int:pk>/', UpdateTodoAPIView.as_view()),
    path('api/todo/create/', CreateTodoAPIView.as_view()),
    path('api/todo/delete/<int:pk>/', DeleteTodoAPIView.as_view()),


]
