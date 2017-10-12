from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from .models import Position

from .forms import PositionDetailCreateForm

# Create your views here.

class PositionListView(ListView):
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

class PositionDetailView(DetailView):
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

class PositionCreateView(CreateView):
	form_class = PositionDetailCreateForm
	template_name = 'form.html'
	# success_url = "/student/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(PositionCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(PositionCreateView, self).get_context_data(*args, **kwargs)
		context['position_name'] = 'Add Position'
		return context

class PositionUpdateView(UpdateView):
	form_class = PositionDetailCreateForm
	template_name = 'Position/detail-update.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(PositionUpdateView, self).get_context_data(*args, **kwargs)
		position_name = self.get_object().position_name
		context['position_name'] = 'Update Position: {position_name}'
		return context

	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)