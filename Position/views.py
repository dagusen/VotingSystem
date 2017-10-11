from django.shortcuts import render

from .models import Position
# Create your views here.

class PostionListView(ListView):
	template_name = 'Postion/position_list.html'
	def get_queryset(self):
		return Postion.objects.filter(user=self.request.user)