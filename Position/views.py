from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from .models import Position

# Create your views here.

class PositionListView(ListView):
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

class PositionDetailView(DetailView):
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)