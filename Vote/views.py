from django.shortcuts import render

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	)

from Candidate.models import Candidate

from PartyList.models import PartyList

class VotePDPLabanListView(ListView):
	queryset = Candidate.objects.filter(party_list__partylist_name__iexact = 'PDP Laban')
	template_name = 'Vote/Votepdplist.html'

class VoteYellowListView(ListView):
	queryset = Candidate.objects.filter(party_list__partylist_name__iexact = 'Yellow Ribbon')
	template_name = 'Vote/Voteyellowlist.html'