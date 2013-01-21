import os, sys
sys.path.append('/home/ubuntu/charades')
os.environ['DJANGO_SETTINGS_MODULE'] = 'charades.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

