from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import CustomUser


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
