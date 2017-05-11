from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    simple_http_code = '<h2>Wiktor to gejaszek!</h2>'
    return HttpResponse(simple_http_code)
