from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
     admin.site.root),

    (r'^(?P<url>about/?)$',
     'django.contrib.flatpages.views.flatpage',
     {},
     'hitzokei_about'),

    (r'',
     include('socialdict.urls')),
)
