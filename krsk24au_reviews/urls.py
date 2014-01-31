__author__ = 'eduard'

from django.conf.urls import patterns, url

from krsk24au_reviews import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='reviews_index'),
                       url(r'^ajax/detailsAboutDay$', views.detailsaboutday, name='detailsAboutDay'),
                       url(r'^ajax/graphForPeriod', views.graph_for_period, name='detailsAboutDay'),
                    )
