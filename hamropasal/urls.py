"""hamropasal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import  include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pasal/', 'pasal.views.show'),
    url(r'^productid/(?P<id>[0-9])/$', 'pasal.views.products'),
    url(r'^register/$', 'pasal.views.contact',name='register'),
    url(r'^register_success/$', 'pasal.views.register_success'),
    url(r'^login/$', 'pasal.views.login'),
    url(r'^auth/$', 'pasal.views.auth_view'),
    url(r'^loggedin/$', 'pasal.views.loggedin'),
    url(r'^invalid/$', 'pasal.views.invalid_login'),
    url(r'^logout/$', 'pasal.views.logout'),
    url(r'^doneContact/$', 'pasal.views.doneContact'),
    url(r'^contactus/$', 'pasal.views.contactus'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
