from django.shortcuts import render
from django.urls import reverse_lazy
from myapp.models import Student
from django.views.generic import *
class StudentListView(ListView):
    model=Student
class StudentDetailView(DetailView):
    model=Student
class StudentCreateView(CreateView):
    model=Student
    fields="__all__"
class StudentUpdateView(UpdateView):
    model=Student
    fields=("name","marks")
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy("students")
