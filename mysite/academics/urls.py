from django.conf.urls import url
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from academics.models import Academics


class AcademicsDetailView(DetailView):
    model = Academics
    # Source of html file
    template_name = 'academics/academics.html'


def detail(request):
    try:
        academics = Academics.objects.all().order_by('-end_date').first()
    except Academics.DoesNotExist:
        raise Http404("Object does not exist")
    return render(request, 'academics/academics.html', {'object': academics})


# What we want to see in /academics
urlpatterns = [
    url(r'^$', detail, name='academics-detail'),
]
