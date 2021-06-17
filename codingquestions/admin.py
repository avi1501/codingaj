from django.contrib import admin
from .models import *
from .models import dataType, questionModel, QuestionDifficulty

from tinymce.widgets import TinyMCE

#  Register your models here.


class richTextField(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {'widget':TinyMCE()}
    }

admin.site.register(dataType)
admin.site.register(questionModel, richTextField)
admin.site.register(QuestionDifficulty)