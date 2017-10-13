from django.conf.urls import url

from .views import (
	VotePDPLabanListView,
	VoteYellowListView,
	)

from PartyList.views import VotePartyListView

from Candidate.views import votes_counter

urlpatterns = [
    url(r'^$', VotePartyListView.as_view(), name='list'),
    url(r'^pdp-laban/$', VotePDPLabanListView.as_view(), name='list'),
    # url(r'^yellow-ribbon/$', VoteYellowListView.as_view(), name='list'),
    #url(r'^(?P<slug>[\w-]+)/$', VotePDPLabanListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VoteYellowListView.as_view(), name='list'),
    url(r'^pdp-laban/(?P<slug>[\w-]+)/$', votes_counter, name='votes_counter'),
]