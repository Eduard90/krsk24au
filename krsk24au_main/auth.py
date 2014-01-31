import logging
from functools import wraps
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
 
 
def http_basic_auth(func):
    """
    Use as a decorator for views that need to perform HTTP basic
    authorisation.
    """
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        if request.META.has_key('HTTP_AUTHORIZATION'):
            try:
                authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
                if authmeth.lower() == 'basic':
                    auth = auth.strip().decode('base64')
                    username, password = auth.split(':', 1)
                    user = authenticate(username=username, password=password)
                    logging.debug('Authenticated %s:%s' % (username, password))
                    if user:
                        login(request, user)
                        logging.debug('Logged in %s:%s' % (username, password))
            except ValueError:
                # Bad HTTP_AUTHORIZATION header
                return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return _decorator