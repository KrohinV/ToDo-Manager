from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User as us

from .serializers import *
from .models import *


@api_view(['POST'])
def create_user(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User(username=username, email=email, password=password)
        user.save()
        return Response("Пользователь создан успешно")
    except Exception as e:
        print(f"Произошла ошибка при создании пользователя: {e}")
        return Response("Произошла ошибка при создании пользователя")

@api_view(['GET'])
def get_all_users(request):
    users_list = User.objects.all()
    serializer = UserSerializer(users_list, many=True)
    return Response({'users': serializer.data})

@api_view(['GET'])
def get_users_by_id(request,id):
    user = User.objects.get(pk=id)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})

@api_view(['PUT', 'PATCH'])
def update_user(request, id):
    user = User.objects.get(pk=id)
    user.username = request.data.get('username')
    user.email = request.data.get('email')
    user.save()
    return Response('Пользователь зменен спешно!')

@api_view(['GET', 'DELETE'])
def del_user(request, id):
    user = User.objects.get(pk=id)
    if request.method == "GET":
        return Response(f"Вы уверены сто хотите удалить пользователя? {user.username}")
    if request.method == "DELETE":
        user.delete()
        return Response("Пользователь удален успешно!")

