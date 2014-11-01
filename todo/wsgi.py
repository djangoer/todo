"""
WSGI config for todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

virtenv =os.path.join(os.environ['HOME'],'webapps','todo','tenv','bin','activate_this.py')
try:
    execfile(virtenv, dict(__file__=virtenv))
except IOError:
    pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
