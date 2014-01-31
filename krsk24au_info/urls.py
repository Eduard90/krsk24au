__author__ = 'eduard'

from django.conf.urls import patterns, url

from krsk24au_info import views

urlpatterns = patterns('',
                       # url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^$', views.UsersView.as_view(), name='users'),
                       url(r'^(?P<pk>\d+)/$', views.UserView.as_view(), name='user'),
                    )
