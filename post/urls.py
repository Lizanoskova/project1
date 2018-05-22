from django.conf.urls import url
from .views import *

from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^(?P<pk>\d+)/$',Post_page.as_view(), name="currentpost"),
    url(r'^new/$',login_required(New_Post.as_view()), name="post_creation"),
    url(r'^(?P<pk>\d+)/edit/$',login_required(Post_Update.as_view()), name="post_update"),
]

