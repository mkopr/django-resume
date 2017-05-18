from django.conf.urls import url
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from basic_info.models import BasicInfo


class BasicInfoDetailView(DetailView):
    model = BasicInfo
    # Source of html file
    template_name = 'basic_info/basic_info.html'


def detail(request):
    try:
        basic_info = BasicInfo.objects.all().order_by('-add_date').first()
    except BasicInfo.DoesNotExist:
        raise Http404("Object does not exist")
    return render(request, 'basic_info/basic_info.html', {'object': basic_info})


# What we want to see in /basic-info
urlpatterns = [
    url(r'^$', detail, name='basic-info-detail'),
]
