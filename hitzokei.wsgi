#!/usr/bin/env python

import os
import site
import sys

site.addsitedir('/srv/www/hitzokei/env/lib/python2.5/site-packages')

sys.path.insert(0, '/srv/www/hitzokei/')
sys.path.insert(0, '/srv/www/hitzokei/hitzokei/apps/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hitzokei.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

