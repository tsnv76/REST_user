from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'date_joined', ]
        # fields = '__all__'
