from django.conf.urls import url

from .views import (
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
)

urlpatterns = [
    url(r'^$', PositionListView.as_view(), name='list'),
    url(r'^create/$', PositionCreateView.as_view(), name='create'),
    # # slug
    #url(r'^(?P<slug>[\w-]+)/$', PositionDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PositionUpdateView.as_view(), name='edit'),
]