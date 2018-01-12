import os
import sys

path='/var/www/Django'
if path not in sys.path:
  sys.path.append(path)

import site
site.addsitedir('/usr/lib/python3.4/dist-packages')


os.environ['DJANGO_SETTINGS_MODULE'] = 'Django.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
