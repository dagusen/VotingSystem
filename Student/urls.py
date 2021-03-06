from django.conf.urls import url

from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
)

urlpatterns = [
    url(r'^$', StudentListView.as_view(), name='list'),
    url(r'^create/$', StudentCreateView.as_view(), name='create'),
    # slug
    #url(r'^(?P<slug>[\w-]+)/$', StudentDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', StudentUpdateView.as_view(), name='edit'),
]