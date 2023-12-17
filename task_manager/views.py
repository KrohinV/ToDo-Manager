from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test

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
def del_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "GET":
        return Response(f"Вы уверены сто хотите удалить пользователя? {user.username}")
    if request.method == "DELETE":
        user.delete()
        return Response("Пользователь удален успешно!")

@require_http_methods(["DELETE"])
@user_passes_test(lambda u: u.is_staff)
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        if request.user.is_staff:
            task.delete()
            return Response({'message': 'Task deleted successfully'})
        else:
            task.is_deleted = True
            task.save()
            return Response({'message': 'Task soft deleted successfully'})
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'})



