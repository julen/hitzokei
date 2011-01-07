#!/usr/bin/env python

import os
import sys

sys.path.insert(0, '/srv/www/hitzokei/')
sys.path.insert(0, '/srv/www/hitzokei/hitzokei/apps/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hitzokei.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

