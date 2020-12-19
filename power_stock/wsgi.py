"""
WSGI config for pos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from power_stock.settings import MEDIA_ROOT, STATIC_ROOT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pos.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
application.add_files(MEDIA_ROOT, prefix='media/')
