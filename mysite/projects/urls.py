from django.conf.urls import url
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import Http404
from projects.models import Projects


class ProjectsDetailView(DetailView):
    model = Projects
    # Source of html file
    template_name = 'projects/projects.html'


def detail(request):
    try:
        projects = Projects.objects.all().order_by('-add_date').first()
    except Projects.DoesNotExist:
        raise Http404("Object does not exist")
    return render(request, 'projects/projects.html', {'object': projects})


# What we want to see in /projects
urlpatterns = [
    url(r'^$', detail, name='projects-detail'),
]
