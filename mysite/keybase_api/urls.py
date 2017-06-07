from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(
        r'(?P<keybase_login>\w{0,39}$)',
        views.get_keybase_data,
        name='keybase_data'
    ),
]
