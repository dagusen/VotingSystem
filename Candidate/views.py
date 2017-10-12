from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from .models import Candidate
from .forms import CandidateDetailCreateForm

class CandidateListView(ListView):
	def get_queryset(self):
		return Candidate.objects.filter(user=self.request.user)

class CandidateDetailView(DetailView):
	def get_queryset(self):
		return Candidate.objects.filter(user=self.request.user)

class CandidateCreateView(CreateView):
	form_class = CandidateDetailCreateForm
	template_name = 'form.html'
	# success_url = "/student/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(CandidateCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(CandidateCreateView, self).get_context_data(*args, **kwargs)
		context['student'] = 'Add Candidate'
		return context

class CandidateUpdateView(UpdateView):
	form_class = CandidateDetailCreateForm
	template_name = 'Candidate/detail-update.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(CandidateUpdateView, self).get_context_data(*args, **kwargs)
		student = self.get_object().student
		context['student'] = 'Update Candidate: {student}'
		return context

	def get_queryset(self):
		return Candidate.objects.filter(user=self.request.user)