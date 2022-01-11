from rest_framework.permissions import DjangoModelPermissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, \
    CreateModelMixin
from rest_framework.decorators import action

from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
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
    default_limit = 10


class ProjectViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # pagination_class = PaginationProject


class ProjectParamFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        project = Project.objects.all()
        if name:
            project = project.filter(name__contains=name)
        return project


class ProjectFiltersViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name']


class PaginationTodo(LimitOffsetPagination):
    default_limit = 20


class ToDoViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    filterset_fields = ['user']
    # pagination_class = PaginationTodo


class UpdateTodoAPIView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @action(methods=['PUT'], detail=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(methods=['PATCH'], detail=True)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DeleteTodoAPIView(RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance


class CreateTodoAPIView(RetrieveModelMixin, CreateModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer

    @action(methods=['POST'], detail=True)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)


class DeleteProjectAPIView(RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    @action(methods=['POST'], detail=True)
    def perform_destroy(self, instance):
        instance.is_active = True
        instance.save()


class CreateProjectAPIView(RetrieveModelMixin, CreateModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    @action(methods=['POST'], detail=True)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)


class UpdateProjectAPIView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    @action(methods=['GET'], detail=True)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @action(methods=['PUT'], detail=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(methods=['PATCH'], detail=True)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class TodoParamFilterViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('text', '')
        text = ToDo.objects.all()
        if name:
            text = text.filter(text__contains=name)
        return text
