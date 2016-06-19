from django.contrib import admin

# from .models import Question
# admin.site.register(Question)

from . import models

admin.site.register(models.Question)
