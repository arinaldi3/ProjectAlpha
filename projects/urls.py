from django.urls import path

from projects.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("", ProjectListView.as_view(), name="list_projects"),
]
