from django.shortcuts import render


def index(request):
    personal_html = 'personal/home.html'
    return render(request, personal_html)
