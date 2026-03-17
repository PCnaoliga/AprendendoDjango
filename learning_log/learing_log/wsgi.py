# Aqui é onde o Django se conecta com o site WEB
# O padrão tradicional para servidores síncronos.
# É o que você usará na maioria das hospedagens comuns.

"""
WSGI config for learing_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learing_log.settings")

application = get_wsgi_application()
