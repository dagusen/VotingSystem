from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from .models import (
	Course,
	)

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CourseDetailCreateForm

# Create your views here.

class CourseListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)

class CourseDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)

class CourseCreateView(LoginRequiredMixin, CreateView):
	form_class = CourseDetailCreateForm
	template_name = 'form.html'
	# success_url = "/student/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(CourseCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(CourseCreateView, self).get_context_data(*args, **kwargs)
		context['course_name'] = 'Add Course'
		return context

class CourseUpdateView(LoginRequiredMixin, UpdateView):
	form_class = CourseDetailCreateForm
	template_name = 'Course/detail-update.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(*args, **kwargs)
		course_name = self.get_object().course_name
		context['course_name'] = 'Update Course: {course_name}'
		return context

	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)