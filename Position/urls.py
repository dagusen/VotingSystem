from django.conf.urls import url

from .views import (
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    PresidentListView,
    VicePresidentListView,
)

urlpatterns = [
	url(r'^President/$', PresidentListView.as_view(), name='list'),
	url(r'^Vice-president/$', VicePresidentListView.as_view(), name='list'),
    url(r'^$', PositionListView.as_view(), name='list'),
    url(r'^create/$', PositionCreateView.as_view(), name='create'),
    # # slug
    #url(r'^(?P<slug>[\w-]+)/$', PositionDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PositionUpdateView.as_view(), name='edit'),
]