from rest_framework import serializers
from .models import Category, Priority, Task, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#
# class ResetPasswordEmailSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
