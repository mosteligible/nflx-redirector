from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("netflix redirector index view")
