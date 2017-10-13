from django.conf.urls import url

from .views import (
    VoteYellowListView,
    VotePDPLabanListView,
    )

from PartyList.views import VotePartyListView

from Candidate.views import votes_counter

urlpatterns = [
    url(r'^$', VotePartyListView.as_view(), name='list'),
<<<<<<< HEAD
    url(r'^pdp-laban/$', VotePDPLabanListView.as_view(), name='list'),
    # url(r'^yellow-ribbon/$', VoteYellowListView.as_view(), name='list'),
    #url(r'^(?P<slug>[\w-]+)/$', VotePDPLabanListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VoteYellowListView.as_view(), name='list'),
    url(r'^pdp-laban/(?P<slug>[\w-]+)/$', votes_counter, name='votes_counter'),
=======
    url(r'^yellow-ribbon/$', VoteYellowListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VotePDPLabanListView.as_view(), name='list'),

>>>>>>> fc095d942ceb10280d603b86cf7b1b14b1054220
]