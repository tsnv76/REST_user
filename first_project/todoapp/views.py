import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.serializers import Serializer, CharField, ValidationError
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response

from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class ToDoAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class PaginationProject(LimitOffsetPagination):
    default_limit = 2


class ProjectViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # filterset_fields = ['Project']
    pagination_class = PaginationProject


class PaginationTodo(LimitOffsetPagination):
    default_limit = 2


class ToDoViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    # filterset_fields = ['Project']
    pagination_class = PaginationTodo

#
# class ProjectSerializer(Serializer):
#     name = CharField(max_length=64)
#     repo_link = CharField(max_length=64)
#     users = CharField(max_length=64)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.repo_link = validated_data.get('repo_link', instance.repo_link)
#         instance.users = validated_data.get('users', instance.users)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         project = Project(**validated_data)
#         project.save()
#         return project
#
#
# class ToDoSerializer(Serializer):
#     text = CharField(max_length=256)
#     project = ProjectSerializer()
#     user = UserModelSerializer()
#
#
# def get_view(request):
#     project = Project.objects.get(pk=1)
#     serializer = ProjectSerializer(project)
#     render = JSONRenderer()
#     json_data = render.render(serializer.data)
#     print(serializer.data)
#     return HttpResponse(json_data)
#
#
# @csrf_exempt
# def post_view(request):
#     print(request.body)
#     data = JSONParser().parse(io.BytesIO(request.body))
#
#     if request.method == 'POST':
#         serializer = ProjectSerializer(data=data)
#     elif request.method == 'PUT':
#         user = Project.objects.get(pk=3)
#         serializer = ProjectSerializer(user, data=data)
#     elif request.method == 'PATCH':
#         user = Project.objects.get(pk=3)
#         serializer = ProjectSerializer(user, data=data, partial=True)
#
#     if serializer.is_valid():
#         print(serializer.validated_data)
#
#         user = serializer.save()
#         serializer = ProjectSerializer(user)
#         render = JSONRenderer()
#         json_data = render.render(serializer.data)
#         print(serializer.data)
#         return HttpResponse(json_data)
#     else:
#         return HttpResponseServerError(serializer.errors['non_field_errors'])