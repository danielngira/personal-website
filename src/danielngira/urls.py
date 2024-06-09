from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", ProjectsListView.as_view(), name="projects_grid"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_details"),
    path("project/create/", ProjectCreateView.as_view(), name="project_create"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
    
]
