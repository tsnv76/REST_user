from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from todoapp.models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    # project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = ields = ['id', 'project', 'text', 'created_date', 'user', 'is_active']
