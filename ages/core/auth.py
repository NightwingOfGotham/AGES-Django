from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect


class AGESUserLogin(object):
    def process_request(self, request):
        # if not request.user.is_authenticated() and not 'new-user' in request.path:
        #     return HttpResponsePermanentRedirect(reverse('new_user'))
        return None