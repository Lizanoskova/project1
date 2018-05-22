from django.conf.urls import url
from blog.views import *

urlpatterns = [

    url(r'^$', Blog_list.as_view(), name="blogview"),
    url(r'^(?P<pk>\d+)/$', blog_page, name="currentblog"),

]
