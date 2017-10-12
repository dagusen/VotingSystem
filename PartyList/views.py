from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)
from .forms import PartyListDetailCreateForm

from .models import PartyList

class PartyListListView(ListView):
	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)

class PartyListDetailView(DetailView):
	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)

class PartyListCreateView(CreateView):
	form_class = PartyListDetailCreateForm
	template_name = 'form.html'
	# success_url = "/student/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(PartyListCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(PartyListCreateView, self).get_context_data(*args, **kwargs)
		context['partylist_name'] = 'Add Party List'
		return context

class PartyListUpdateView(UpdateView):
	form_class = PartyListDetailCreateForm
	template_name = 'PartyList/detail-update.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(PartyListUpdateView, self).get_context_data(*args, **kwargs)
		partylist_name = self.get_object().partylist_name
		context['partylist_name'] = 'Update Party List: {partylist_name}'
		return context

	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)