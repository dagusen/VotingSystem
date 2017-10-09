from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import (
	Student,
	Course,
	Department,
	)

from .forms import (
	StudentDetailCreateForm,
	)
# Create your views here.

class StudentListView(ListView):
	def get_queryset(self):
		return Student.objects.filter(user=self.request.user)

class StudentDetailView(DetailView):
	def get_queryset(self):
		return Student.objects.filter(user=self.request.user)

class StudentCreateView(CreateView):
	form_class = StudentDetailCreateForm
	template_name = 'form.html'
	success_url = "/student/"

class CourseListView(ListView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)

class CourseDetailView(DetailView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)

class DepartmentListView(ListView):
	def get_queryset(self):
		return Department.objects.filter(user=self.request.user)

class DepartmentDetailView(DetailView):
	def get_queryset(self):
		return Department.objects.filter(user=self.request.user)