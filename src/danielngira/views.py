from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Project
from .forms import ProjectForm
from django.urls import reverse_lazy


def home(request):
    return render(request, "danielngira/home.html")
    
class ProjectsListView(ListView):
    model = Project
    template_name = "danielngira/project_grid.html"
    context_object_name = "projects"
    ordering = ["-year"]
    paginate_by = 5

class ProjectDetailView(DetailView):
    model = Project
    template_name = "danielngira/project_details.html"

    def get_success_url(self):
        return reverse_lazy("project_details", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "danielngira/project_grid.html"
    success_url = reverse_lazy("projects_grid")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = True
        return context

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "danielngira/project_form.html"

    def get_success_url(self):
        return reverse_lazy("project-detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = False
        return context

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "danielngira/project_confirm_delete.html"
    success_url = reverse_lazy("project_grid")

