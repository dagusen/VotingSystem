from django.shortcuts import render


from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from .models import Department

from .forms import DepartmentDetailCreateForm

# Create your views here.

class DepartmentListView(ListView):
	def get_queryset(self):
		return Department.objects.filter(user=self.request.user)

class DepartmentDetailView(DetailView):
	def get_queryset(self):
		return Department.objects.filter(user=self.request.user)

class DepartmentCreateView(CreateView):
	form_class = DepartmentDetailCreateForm
	template_name = 'form.html'
	# success_url = "/student/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(DepartmentCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(DepartmentCreateView, self).get_context_data(*args, **kwargs)
		context['department_name'] = 'Add Department'
		return context

class DepartmentUpdateView(UpdateView):
	form_class = DepartmentDetailCreateForm
	template_name = 'Department/detail-update.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(DepartmentUpdateView, self).get_context_data(*args, **kwargs)
		department_name = self.get_object().department_name
		context['department_name'] = 'Update Department: {department_name}'
		return context

	def get_queryset(self):
		return Department.objects.filter(user=self.request.user)