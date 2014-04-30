from django.conf.urls import patterns, include, url

from django.contrib import admin
from view import *
from books import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$',current_datetime),
    url(r'^test/$',test_request),
    url(r'^testup/$',test_upload),
    # url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
)
