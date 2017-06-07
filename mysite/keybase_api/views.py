from django.http import HttpResponse

from .models import KeybaseKey
from .utils import request_keybase_user


def get_keybase_data(request, keybase_login):
    try:
        user = KeybaseKey.objects.get(login=keybase_login)
    except KeybaseKey.DoesNotExist:
        user_data = request_keybase_user(keybase_login)
        user = KeybaseKey(
            login=user_data['login'],
            publick_key=user_data['pgp_key'],
        )
        user.save()

    return HttpResponse(status=200)
