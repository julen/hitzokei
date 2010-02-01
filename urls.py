from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from socialdict.feeds import LatestEntriesFeed
feeds = { 'entries': LatestEntriesFeed }

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$',
     'django.views.generic.simple.direct_to_template',
     { 'template': 'homepage.html' },
     'hitzokei_home'),

    (r'^static/(?P<path>.*)$',
     'django.views.static.serve',
     { 'document_root': settings.MEDIA_ROOT }),

    (r'^admin/',
     include(admin.site.urls)),

    (r'^feed/(?P<url>.*)/$',
     'django.contrib.syndication.views.feed',
     { 'feed_dict': feeds }),

    (r'^(?P<url>about/?)$',
     'django.contrib.flatpages.views.flatpage',
     {},
     'hitzokei_about'),

    (r'',
     include('socialdict.urls')),
)
