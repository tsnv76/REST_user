from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todoapp.views import ProjectViewSet, ToDoViewSet, get_view, post_view
from users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('Project', ProjectViewSet)
router.register('ToDo', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/get/', get_view),
    path('api/post/', post_view)
]
