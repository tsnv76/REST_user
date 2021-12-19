from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.decorators import action


class UserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
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


class Pagination(LimitOffsetPagination):
    default_limit = 2


class UserViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    # filterset_fields = ['first_name']
    # pagination_class = Pagination
    #
    # @action(methods=['GET'], detail=True)
    # def get_user_name(self, request, pk=None):
    #     author = CustomUser.objects.get(pk=pk)
    #     return Response({'id': str(pk)})