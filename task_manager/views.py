from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *
from .filters import TaskFilter


def del_entry(request, queryset):
    if request.user.is_admin == False:
        queryset.deleted = True
        queryset.save()
        return Response("Удалено успешно!")
    else:
        queryset.delete()
        return Response("Удалено успешно!")


"""_________  USER _____________"""
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("Пользователь создан успешно")
#     return Response("Произошла ошибка при создании пользователя")

class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET'])
# def get_all_users(request):
#     users_list = User.objects.all()
#     serializer = UserSerializer(users_list, many=True)
#     return Response({'users': serializer.data})

class GetAllUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def get_users_by_id(request, id):
    user = User.objects.get(pk=id)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})


# @api_view(['PUT', 'PATCH'])
# def update_user(request, id):
#     user = User.objects.get(pk=id)
#
#     if request.method == 'PUT':
#         serializer = UserSerializer(user, request.data)
#     elif request.method == 'PATCH':
#         serializer = UserSerializer(user, data=request.data, partial=True)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response('Пользователь изменен успешно!')
#
#     return Response(serializer.errors)

class UpdateUser(generics.UpdateAPIView):
    serializers=User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['GET', 'DELETE'])
def del_user(request, id):
    user = User.objects.get(pk=id)
    if request.method == "GET":
        return Response(f"Вы уверены что хотите удалить пользователя? '{user.username}'")
    if request.method == "DELETE":
        del_entry(request, user)


"""_________  TASK _____________"""
# @api_view(['POST'])
# def create_task(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("Задача создана успешно")
#     return Response(serializer.errors)

class CreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


# @api_view(['GET'])
# def get_all_tasks(request):
#     tasks_list = Task.objects.all()
#     serializer = TaskSerializer(tasks_list, many=True)
#
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ['status']
#
#     return Response({'tasks': serializer.data})

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all().order_by('created_at')
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['-status']
    permission_classes = (IsAuthenticated,)


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
    task = Task.objects.filter(user=id)
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


# @api_view(['PUT', 'PATCH'])
# def update_task(request, id):
#     task = Task.objects.get(pk=id)
#
#     if request.method == 'PUT':
#         serializer = TaskSerializer(task, request.data)
#     elif request.method == 'PATCH':
#         serializer = TaskSerializer(task, data=request.data, partial=True)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response('Задача изменена успешно!')
#
#     return Response(serializer.errors)

class UpdateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['GET', 'DELETE'])
def del_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == "GET":
        return Response(f"Вы уверены что хотите удалить задачу? '{task.title}'")
    if request.method == "DELETE":
        del_entry(request, task)


"""_________  CATEGORY _____________"""

# @api_view(['POST'])
# def create_category(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("Категория создана успешно")
#     return Response(serializer.errors)

class CreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


@api_view(['GET'])
def get_category_by_id(request, id):
    category = Category.objects.get(pk=id)
    serializer = CategorySerializer(category)
    return Response({'category': serializer.data})


# @api_view(['PUT', 'PATCH'])
# def update_category(request, id):
#     category = Category.objects.get(pk=id)
#
#     if request.method == 'PUT':
#         serializer = CategorySerializer(category, request.data)
#     elif request.method == 'PATCH':
#         serializer = CategorySerializer(category, data=request.data, partial=True)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response('Категория изменена успешно!')
#
#     return Response(serializer.errors)

class UpdateCategory(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


@api_view(['GET', 'DELETE'])
def del_category(request, id):
    category = Category.objects.get(pk=id)
    if request.method == "GET":
        return Response(f"Вы уверены что хотите удалить категорию? '{category.name}'")
    if request.method == "DELETE":
        del_entry(request, category)


"""_________  PRIORITY _____________"""

# @api_view(['POST'])
# def create_priority(request):
#     serializer = PrioritySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("Приоретет создан успешно")
#     return Response(serializer.errors)
class CreatePriority(generics.ListCreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (IsAuthenticated,)

@api_view(['GET'])
def get_priority_by_id(request, id):
    priority = Priority.objects.get(pk=id)
    serializer = PrioritySerializer(priority)
    return Response({'priority': serializer.data})


# @api_view(['PUT', 'PATCH'])
# def update_priority(request, id):
#     priority = Priority.objects.get(pk=id)
#
#     if request.method == 'PUT':
#         serializer = PrioritySerializer(priority, request.data)
#     elif request.method == 'PATCH':
#         serializer = PrioritySerializer(priority, data=request.data, partial=True)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response('Приоретет изменен успешно!')
#
#     return Response(serializer.errors)
class UpdatePriority(generics.UpdateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (IsAuthenticated,)

@api_view(['GET', 'DELETE'])
def del_priority(request, id):
    priority = Priority.objects.get(pk=id)
    if request.method == "GET":
        return Response(f"Вы уверены что хотите удалить категорию? '{priority.name}'")
    if request.method == "DELETE":
        del_entry(request, priority)
