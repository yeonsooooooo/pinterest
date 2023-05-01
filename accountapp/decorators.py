import args as args
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        #pk를 가진 사람이 pk가 됨
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated