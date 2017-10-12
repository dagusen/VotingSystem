from django.conf.urls import url

from .views import (
    CandidateListView,
    CandidateDetailView,
    CandidateCreateView,
    CandidateUpdateView,
)

urlpatterns = [
    url(r'^$', CandidateListView.as_view(), name='list'),
    url(r'^create/$', CandidateCreateView.as_view(), name='create'),
    # # slug
    #url(r'^(?P<slug>[\w-]+)/$', CandidateDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', CandidateUpdateView.as_view(), name='edit'),
]