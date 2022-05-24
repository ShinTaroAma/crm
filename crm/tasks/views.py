from django.shortcuts import render


def project(request, pk):
    pass


def projects(request):
    return render(request, 'tasks/projects.html')


def home(request):
    return render(request, 'tasks/home.html')
