"""
WSGI config for BEAM_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BEAM_project.settings')

application = get_wsgi_application()
application=WhiteNoise(application,root=os.path.join(ROOT_DIR,'staticfiles')) 
 