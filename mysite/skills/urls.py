from django.conf.urls import url
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from skills.models import Skills


class SkillsDetailView(DetailView):
    model = Skills
    # Source of html file
    template_name = 'skills/skills.html'


def detail(request):
    try:
        skills = Skills.objects.all().order_by('name').first()
    except Skills.DoesNotExist:
        raise Http404("Object does not exist")
    return render(request, 'skills/skills.html', {'object': skills})


# What we want to see in /skills
urlpatterns = [
    url(r'^$', detail, name='skills-detail'),
]
