from .views import UserModelViewSet
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(r'', UserModelViewSet.as_view({'get': 'list'}))
]