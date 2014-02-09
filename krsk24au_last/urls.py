__author__ = 'eduard'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from krsk24au_last import views

urlpatterns = patterns('',
                       # url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^$', login_required(views.AllNewUsersView.as_view()), name='newusers_index'),
                       # url(r'^(?P<pk>\d+)/$', login_required(views.UserView.as_view()), name='user'),
                    )
