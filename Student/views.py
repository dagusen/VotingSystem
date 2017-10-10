from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from .models import (
	Student,
	Course,
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
	# success_url = "/student/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(StudentCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(StudentCreateView, self).get_context_data(*args, **kwargs)
		context['name'] = 'Add Student'
		return context

class StudentUpdateView(UpdateView):
	form_class = StudentDetailCreateForm
	template_name = 'Student/detail-update.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(*args, **kwargs)
		First_name = self.get_object().First_name
		context['First_name'] = 'Update Student: {First_name}'
		return context

	def get_queryset(self):
		return Student.objects.filter(user=self.request.user)

class CourseListView(ListView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)
