from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', ]
        # fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance = validated_data.get('users', instance)
    #     instance.save()
    #     return instance
