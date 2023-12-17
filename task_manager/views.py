from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.models import User as us

from .serializers import *
from .models import *


#  _________  USER _____________
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Пользователь создан успешно")
    return Response("Произошла ошибка при создании пользователя")


@api_view(['GET'])
def get_all_users(request):
    users_list = User.objects.all()
    serializer = UserSerializer(users_list, many=True)
    return Response({'users': serializer.data})


@api_view(['GET'])
def get_users_by_id(request, id):
    user = User.objects.get(pk=id)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})


@api_view(['PUT', 'PATCH'])
def update_user(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'PUT':
        serializer = UserSerializer(user, request.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response('Пользователь изменен успешно!')

    return Response(serializer.errors)


@api_view(['GET', 'DELETE'])
def del_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "GET":
        return Response(f"Вы уверены сто хотите удалить пользователя? {user.username}")
    if request.method == "DELETE":
        user.delete()
        return Response("Пользователь удален успешно!")


#  _________  TASK _____________
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Задача создана успешно")
    return Response(serializer.errors)


@api_view(['GET'])
def get_all_tasks(request):
    tasks_list = Task.objects.all()
    serializer = TaskSerializer(tasks_list, many=True)
    return Response({'tasks': serializer.data})


@api_view(['GET'])
def get_task_by_status(request, status):
    """
    status values can be: TODO, INPROGRESS, DONE
    """
    task = Task.objects.filter(status=status)
    serializer = TaskSerializer(task, many=True)
    return Response({'status_tasks': serializer.data})


@api_view(['GET'])
def get_task_for_user(request, id):
    task = Task.objects.filter(created_by=id)
    serializer = TaskSerializer(task, many=True)
    return Response({'user_tasks': serializer.data})


@api_view(['GET'])
def get_task_for_category(request, id):
    task = Task.objects.filter(category_id=id)
    serializer = TaskSerializer(task, many=True)
    return Response({'category_tasks': serializer.data})


@api_view(['GET'])
def get_task_for_priority(request, id):
    task = Task.objects.filter(priority_id=id)
    serializer = TaskSerializer(task, many=True)
    return Response({'priority_tasks': serializer.data})


@api_view(['GET'])
def get_task_for_id(request, id):
    task = Task.objects.filter(pk=id)
    serializer = TaskSerializer(task, many=True)
    return Response({'task': serializer.data})


@api_view(['PUT', 'PATCH'])
def update_task(request, id):
    task = Task.objects.get(pk=id)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, request.data)
    elif request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response('Задача изменена успешно!')

    return Response(serializer.errors)


#  _________  CATEGORY _____________

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Категория создана успешно")
    return Response(serializer.errors)


@api_view(['GET'])
def get_category_by_id(request, id):
    category = Category.objects.get(pk=id)
    serializer = CategorySerializer(category)
    return Response({'category': serializer.data})


@api_view(['PUT', 'PATCH'])
def update_category(request, id):
    category = Category.objects.get(pk=id)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, request.data)
    elif request.method == 'PATCH':
        serializer = CategorySerializer(category, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response('Категория изменена успешно!')

    return Response(serializer.errors)


#  _________  PRIORITY _____________

@api_view(['POST'])
def create_priority(request):
    serializer = PrioritySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Приоретет создан успешно")
    return Response(serializer.errors)


@api_view(['GET'])
def get_priority_by_id(request, id):
    priority = Priority.objects.get(pk=id)
    serializer = PrioritySerializer(priority)
    return Response({'priority': serializer.data})


@api_view(['PUT', 'PATCH'])
def update_priority(request, id):
    priority = Priority.objects.get(pk=id)

    if request.method == 'PUT':
        serializer = PrioritySerializer(priority, request.data)
    elif request.method == 'PATCH':
        serializer = PrioritySerializer(priority, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response('Приоретет изменен успешно!')

    return Response(serializer.errors)
