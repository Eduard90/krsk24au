__author__ = 'eduard'

from django.conf.urls import patterns, url

from krsk24au_search import views

urlpatterns = patterns('',
                       # url(r'^$', views.IndexView.as_view(), name='index'),
                       # url(r'^$', views.IndexView.as_view(), name='searchIndex'),
                       url(r'^$', views.index, name='search_index'),
                       # url(r'^(?P<pk>\d+)/$', views.UserView.as_view(), name='user'),
                    )
