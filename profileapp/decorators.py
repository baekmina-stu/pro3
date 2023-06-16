
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_decorator(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated
