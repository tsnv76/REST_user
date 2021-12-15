import io

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer, CharField, ValidationError

from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, TodoModelSerializer
from users.serializers import UserSerializer


class ProjectViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectSerializer(Serializer):
    name = CharField(max_length=64)
    repo_link = CharField(max_length=64)
    users = CharField(max_length=64)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.repo_link = validated_data.get('repo_link', instance.repo_link)
        instance.users = validated_data.get('users', instance.users)
        instance.save()
        return instance

    def create(self, validated_data):
        project = Project(**validated_data)
        project.save()
        return project


class ToDoSerializer(Serializer):
    text = CharField(max_length=256)
    project = ProjectSerializer()
    user = UserSerializer()


def get_view(request):
    project = Project.objects.get(pk=1)
    serializer = ProjectSerializer(project)
    render = JSONRenderer()
    json_data = render.render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data)


@csrf_exempt
def post_view(request):
    print(request.body)
    data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = ProjectSerializer(data=data)
    elif request.method == 'PUT':
        user = Project.objects.get(pk=3)
        serializer = ProjectSerializer(user, data=data)
    elif request.method == 'PATCH':
        user = Project.objects.get(pk=3)
        serializer = ProjectSerializer(user, data=data, partial=True)

    if serializer.is_valid():
        print(serializer.validated_data)

        user = serializer.save()
        serializer = ProjectSerializer(user)
        render = JSONRenderer()
        json_data = render.render(serializer.data)
        print(serializer.data)
        return HttpResponse(json_data)
    else:
        return HttpResponseServerError(serializer.errors['non_field_errors'])