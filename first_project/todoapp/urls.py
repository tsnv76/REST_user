from .views import ProjectModelViewSet
from django.urls import path

app_name = 'todoapp'

urlpatterns = [
    path(r'', ProjectModelViewSet.as_view({'get': 'list'}))
]