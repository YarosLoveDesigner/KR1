from django.shortcuts import render
from .models import Building, Project

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'building_list.html', {'buildings': buildings})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})