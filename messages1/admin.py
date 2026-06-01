from django.contrib import admin

# Register your models here.
from .models import Student,Quiz, Question, Result
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Result)
