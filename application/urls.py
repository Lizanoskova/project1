"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from core.views import Main_page, RegisterFormView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth.views import logout


urlpatterns = [

    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginView.as_view(template_name = 'core/login.html'),name = 'login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^$', Main_page.as_view(),name = 'main'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blogs')),
    url(r'^post/', include('post.urls', namespace='posts')),
    url(r'^category/', include('category.urls', namespace='categories')),
]




