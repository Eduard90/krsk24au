__author__ = 'eduard'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from krsk24au_info import views

urlpatterns = patterns('',
                       # url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^$', login_required(views.UsersView.as_view()), name='users'),
                       url(r'^(?P<pk>\d+)/$', login_required(views.UserView.as_view()), name='user'),
                    )
