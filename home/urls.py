from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$',views.logout, name='logout'),
]
