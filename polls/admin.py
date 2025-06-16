from django.contrib import admin
from .models import question_cls,choice_cls
# Register your models here.

admin.site.register(question_cls)
admin.site.register(choice_cls)