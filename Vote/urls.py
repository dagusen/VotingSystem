from django.conf.urls import url

from .views import (
    VoteYellowListView,
    VotePDPLabanListView,
    )

from PartyList.views import VotePartyListView


urlpatterns = [
    url(r'^$', VotePartyListView.as_view(), name='list'),
    url(r'^yellow-ribbon/$', VoteYellowListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VotePDPLabanListView.as_view(), name='list'),

]