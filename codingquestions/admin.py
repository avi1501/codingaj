from django.contrib import admin
from .models import dataType, questionModel, QuestionDifficulty

#  Register your models here.

admin.site.register(dataType)
admin.site.register(questionModel)
admin.site.register(QuestionDifficulty)