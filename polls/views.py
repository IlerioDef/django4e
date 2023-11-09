from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 94ae76ab is the polls index.")
