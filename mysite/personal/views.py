from django.shortcuts import render
from .models import WelcomeText, Academics, BasicInfo, Experience, Projects, \
    Skills


def index(request):
    personal_html = 'personal/home.html'
    welcome_text = WelcomeText.objects.first()
    academics = Academics.objects.first()
    basic_info = BasicInfo.objects.get(first_name='Marcin')
    experience_1 = Experience.objects.get(company_name='Delivery Service')
    experience_2 = Experience.objects.get(company_name='Law Office')
    skills = Skills.objects.first()
    project_1 = Projects.objects.get(name='morg')
    project_2 = Projects.objects.get(name='django-resume')

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
        },
    )