from django.contrib import admin
from .models import Category, Priority, Task, User

admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(User)