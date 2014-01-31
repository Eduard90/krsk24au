from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'krsk24au.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'krsk24au_main/auth.html'}),
    url(r'^accounts/logout/$', 'krsk24au_main.views.logoutview', name='logout'),
    # url(r'^accounts/login/$', 'krsk24au_main.views.loginview', name='login'),
    url(r'^$', include('krsk24au_main.urls')),
    url(r'^user/', include('krsk24au_info.urls')),
    url(r'^search/', include('krsk24au_search.urls')),
    url(r'^reviews/', include('krsk24au_reviews.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
