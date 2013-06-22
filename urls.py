from django.conf.urls import include, patterns, url
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from socialdict.feeds import LatestEntriesFeed
feeds = { 'entries': LatestEntriesFeed }


urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='homepage.html'),
        name='hitzokei_home'),

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
