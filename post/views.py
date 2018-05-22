# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,reverse,redirect
from .models import Post
from comment.models import Comment
from django.views.generic import CreateView,UpdateView

class Post_Update(UpdateView):

   template_name = 'post/edit_post.html'
   model = Post
   fields = 'title', 'text'

   def get_queryset(self):
      return super(Post_Update, self).get_queryset().filter(author = self.request.user)
   def get_success_url(self):
      return reverse('posts:currentpost',kwargs={'pk': self.object.pk})



class New_Post(CreateView):

   template_name = 'post/new_post.html'
   model = Post
   fields = 'title', 'text'

   def get_success_url(self):
      return reverse('posts:currentpost',kwargs={'pk': self.object.pk})

   def form_valid(self,form):
      form.instance.author = self.request.user
      form.instance.blog_id = self.request.user.id
      return super(New_Post, self).form_valid(form)


class Post_page(CreateView):

    template_name = "post/post_page.html"
    model = Comment
    fields = ('text',)


    def get_context_data(self, **kwargs):
        context = super(Post_page, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        #return redirect(self.request.META['HTTP_REFERER'])
       return reverse('posts:currentpost',pk=self.kwargs.get('pk'))


    def form_valid(self, form):
       form.instance.author = self.request.user
       form.instance.post_id = self.kwargs.get('pk')
       return super(Post_page, self).form_valid(form)




# Create your views here.
