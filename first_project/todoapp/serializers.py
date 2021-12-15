from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from todoapp.models import Project, ToDo


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(serializers.ModelSerializer):
    project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'

