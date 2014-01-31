__author__ = 'eduard'

from django.conf.urls import patterns, url

from krsk24au_main import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                    )
