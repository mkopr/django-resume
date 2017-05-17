from django.conf.urls import url
from django.views.generic import DetailView
from basic_info.models import BasicInfo


class BasicInfoDetailView(DetailView):
    model = BasicInfo
    # Source of html file
    template_name = 'basic_info/basic_info.html'

# What we want to see in /basic-info
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BasicInfoDetailView.as_view(),
        name='basic-info-detail')
    ]
