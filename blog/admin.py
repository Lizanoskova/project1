# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = 'id', 'title',
    list_editable = 'title',

#@admin.register(Answer)
#class AnswerAdmin(admin.ModelAdmin):
   # pass



# Register your models here.
