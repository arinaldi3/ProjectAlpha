# from distutils.log import Log
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.urls import reverse_lazy


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["is_completed"]

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.user = self.request.user
        plan.save()
        form.save_m2m
        return redirect("show_my_tasks")

    # def get_success_url(self):
    #     return reverse_lazy("show_my_tasks", args=[self.object.id])
