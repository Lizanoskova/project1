# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.views.generic.edit import FormView
from post.models import Category, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.shortcuts import render,reverse,redirect


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")



class RegisterFormView(FormView):

    form_class = UserCreationForm
    success_url = "login"
    template_name = "core/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main')


class Main_page(ListView):
        model = Category
        context_object_name = 'categories'
        template_name = "core/base.html"


