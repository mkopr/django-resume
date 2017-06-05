from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(
        r'(?P<github_login>\w{0,39}$)',
        views.get_github_data,
        name='github_data'
    ),
]
