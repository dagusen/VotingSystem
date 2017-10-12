from django.conf.urls import url

from .views import (
    PartyListListView,
    PartyListDetailView,
    PartyListCreateView,
    PartyListUpdateView,
)

urlpatterns = [
    url(r'^$', PartyListListView.as_view(), name='list'),
    url(r'^create/$', PartyListCreateView.as_view(), name='create'),
    # # slug
    #url(r'^(?P<slug>[\w-]+)/$', PartyListDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PartyListUpdateView.as_view(), name='edit'),
]