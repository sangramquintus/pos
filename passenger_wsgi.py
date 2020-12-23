import imp
import os
import sys

SCRIPT_NAME = ''


class PassengerPathInfoFix(object):
    """
    Sets PATH_INFO from REQUEST_URI since Passenger doesn't provide it.
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        from urllib.parse import unquote
        environ['SCRIPT_NAME'] = SCRIPT_NAME

        request_uri = unquote(environ['REQUEST_URI'])
        script_name = unquote(environ.get('SCRIPT_NAME', ''))
        offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
        environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
        return self.app(environ, start_response)


os.environ['DJANGO_PRODUCTION'] = 'True'
sys.path.insert(0, os.path.dirname(__file__))
wsgi = imp.load_source('wsgi', '/home/quintus1/pos.quintuslabs.in/pos/power_stock/wsgi.py')
application = wsgi.application
application = PassengerPathInfoFix(application)

# import os
# import sys
#
# cwd = os.getcwd()
# sys.path.append(cwd)
# print('Current Dir ->' + cwd)
# import EatLoads.wsgi as eatload_wsgi
# os.environ['DJANGO_PRODUCTION'] = 'True'
# application = eatload_wsgi.application
