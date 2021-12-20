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
