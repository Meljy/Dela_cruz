from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class PatientListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/patient_list.html'

class PatientDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/patient_detail.html'

class PatientCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/patient_create.html'

class PatientUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/patient_update.html'

class PatientDeleteView(DeleteView):
    model = Post
    template_name = 'app/patient_delete.html'
    success_url = reverse_lazy('home')