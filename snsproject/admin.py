from django.contrib import admin
from .models import SnsModel, Comment, TodoModel
# Register your models here.
admin.site.register(SnsModel)
admin.site.register(Comment)
admin.site.register(TodoModel)