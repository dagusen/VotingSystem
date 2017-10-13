from django.conf.urls import url

from .views import (
	VotePDPLabanListView,
	VoteYellowListView,
	)

from PartyList.views import VotePartyListView


urlpatterns = [
    url(r'^$', VotePartyListView.as_view(), name='list'),
    url(r'^pdp-laban/$', VotePDPLabanListView.as_view(), name='list'),
    # url(r'^yellow-ribbon/$', VoteYellowListView.as_view(), name='list'),
    #url(r'^(?P<slug>[\w-]+)/$', VotePDPLabanListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VoteYellowListView.as_view(), name='list'),
    #url(r'^create/$', PartyListCreateView.as_view(), name='create'),
    # # slug
    #url(r'^(?P<slug>[\w-]+)/$', PartyListDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/$', PartyListUpdateView.as_view(), name='edit'),
]