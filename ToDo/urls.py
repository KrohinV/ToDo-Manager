from django.contrib import admin
from django.urls import path, include
from rest_framework import urls

from task_manager.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/user/create', create_user, name='create_user'),
    path('api/v1/user/get_all', get_all_users, name='get_users'),
    path('api/v1/user/get/<int:id>', get_users_by_id, name='get_user'),
    path('api/v1/user/update/<int:id>', update_user, name='update_user'),
    path('api/v1/user/delete/<int:id>', del_user, name='delete_user'),
    path('api/v1/user/', include('rest_framework.urls')),
   ]