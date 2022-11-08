from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView


import todoapp
import users
from todoapp.views import ProjectViewSet, ToDoViewSet, ProjectAPIView, ToDoAPIView, UpdateProjectAPIView, \
    UpdateTodoAPIView, CreateProjectAPIView, DeleteProjectAPIView, CreateTodoAPIView, DeleteTodoAPIView, \
    ProjectParamFilterViewSet, TodoParamFilterViewSet
from users.views import UserViewSet, UserAPIView, UpdateUserAPIView, CreateUserAPIView

schema_view = get_schema_view(
    openapi.Info(
        title='Todo List',
        default_version='v1',
        description='',
        contact=openapi.Contact(email='test@test.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

router = DefaultRouter()
router.register('users', UserViewSet, basename=users)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)
router.register('project_filters', ProjectParamFilterViewSet)
router.register('todo_filters', TodoParamFilterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/users/', UserViewSet.as_view({'get': 'list'})),
    path('api/users/<int:pk>/', UserAPIView.as_view()),
    path('api/users/update/<int:pk>/', UpdateUserAPIView.as_view()),
    path('api/project/', ProjectViewSet.as_view({'get': 'list'})),
    path('api/project/<int:pk>/', ProjectAPIView.as_view()),
    path('api/project/update/<int:pk>/', UpdateProjectAPIView.as_view()),
    path('api/project/create/', CreateProjectAPIView.as_view()),
    path('api/users/create/', CreateUserAPIView.as_view()),
    path('api/project/delete/<int:pk>/', DeleteProjectAPIView.as_view()),
    path('api/todo/', ToDoViewSet.as_view({'get': 'list'})),
    path('api/todo/<int:pk>/', ToDoAPIView.as_view()),
    path('api/todo/update/<int:pk>/', UpdateTodoAPIView.as_view()),
    path('api/todo/create/', CreateTodoAPIView.as_view()),
    path('api/todo/delete/<int:pk>/', DeleteTodoAPIView.as_view()),

    # re_path(r'^api/(?P<version>.\d)', ProjectViewSet.as_view({'get': 'list'})),
    # path('api/project/v1', include('todoapp.urls', namespace='v1')),
    # path('api/project/v2', include('todoapp.urls', namespace='v2')),

    re_path(r'^api/(?P<version>.\d)', UserViewSet.as_view({'get': 'list'})),
    path('api/users/v1', include('users.urls', namespace='v1')),
    path('api/users/v2', include('users.urls', namespace='v2')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0)),

    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', TemplateView.as_view(template_name='index.html')),

]
