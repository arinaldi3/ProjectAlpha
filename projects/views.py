from django.shortcuts import render
from django.views.generic.list import ListView
from projects.models import Project
from django.urls import reverse_lazy


# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
