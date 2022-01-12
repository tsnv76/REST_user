from rest_framework.permissions import BasePermission, DjangoModelPermissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.decorators import action


# class CustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_superuser)


class UserModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [DjangoModelPermissions]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer


class UserAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class Pagination(LimitOffsetPagination):
    default_limit = 2


class UserViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    # filterset_fields = ['first_name']
    # pagination_class = Pagination


class UpdateUserAPIView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer

    @action(methods=['PUT'], detail=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(methods=['PATCH'], detail=True)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
