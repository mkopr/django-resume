from django.conf.urls import url
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from experience.models import Experience


class ExperienceDetailView(DetailView):
    model = Experience
    # Source of html file
    template_name = 'experience/experience.html'


def detail(request):
    try:
        experience = Experience.objects.all().order_by('-end_date').first()
    except Experience.DoesNotExist:
        raise Http404("Object does not exist")
    return render(request, 'experience/experience.html', {'object': experience})


# What we want to see in /experience
urlpatterns = [
    url(r'^$', detail, name='experience-detail'),
]
