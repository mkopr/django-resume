from django.shortcuts import render
from .models import WelcomeText, Academics, BasicInfo, Experience, Projects, \
    Skills
from github_api.models import GithubUser, GithubRepo
from keybase_api.models import KeybaseKey


def index(request):
    personal_html = 'personal/header.html'
    welcome_text = WelcomeText.objects.first()
    academics = Academics.objects.first()
    basic_info = BasicInfo.objects.get(id=1)
    experience_1 = Experience.objects.get(id=1)
    experience_2 = Experience.objects.get(id=2)
    skills = Skills.objects.first()
    project_1 = Projects.objects.get(id=1)
    project_2 = Projects.objects.get(id=2)

    # Take date about github from data base
    github_user = GithubUser.objects.last()
    github_repo = GithubRepo.objects.all()

    # Take data about keybase from data base
    keybase = KeybaseKey.objects.last()

    return render(
        request=request,
        template_name=personal_html,
        context={
            'welcome_text': welcome_text,
            'basic_info': basic_info,
            'academics': academics,
            'experience_1': experience_1,
            'experience_2': experience_2,
            'skills': skills,
            'project_1': project_1,
            'project_2': project_2,

            # Take date about github from data base
            'github_user': github_user,
            'github_repo': github_repo,

            # Take data about keybase from data base
            'keybase': keybase,
        },
    )