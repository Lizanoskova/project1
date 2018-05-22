# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Blog
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404

class Blog_list(ListView):

    model = Blog
    context_object_name = 'blogs'
    template_name = "blog/blog_list.html"

#class Blog_page(ListView):

    #model = Blog
    #context_object_name = 'blog'
    #template_name = "blog/blog_page.html"

def blog_page(request, pk=None):
    blog = get_object_or_404(Blog.objects, pk=pk)
    return render(request, 'blog/blog_page.html', {'blog': blog})
# Create your views here.
