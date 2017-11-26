from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name='forum'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^create$',views.createPost, name='createPost'),
    url(r'^(?P<post_id>[0-9]+)$',views.viewpost, name='post'),
]
