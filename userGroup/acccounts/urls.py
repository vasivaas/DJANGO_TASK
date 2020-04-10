from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    url(r'group/$', views.group_list, name="all_group"),
    url(r'group/(?P<pk>\d+)$', views.view_group_info, name="group_info"),
    url(r'user/(?P<pk>\d+)$', views.view_user_info, name="user_info"),
    url(r'^create/$', views.UserCreate.as_view(), name='user_create'),
    url(r'^user/(?P<pk>\d+)/update/$', views.UserUpdate.as_view(), name='user_update'),
    url(r'^user/(?P<pk>\d+)/delete/$', views.UserDelete.as_view(), name='user_delete'),
    url(r'^group/create/$', views.GroupCreate.as_view(), name='group_create'),
    url(r'^group/(?P<pk>\d+)/update/$', views.GroupUpdate.as_view(), name='group_update'),
    url(r'^group/(?P<pk>\d+)/delete/$', views.GroupDelete.as_view(), name='group_delete'),
]