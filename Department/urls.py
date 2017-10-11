from django.conf.urls import url

from .views import (
    DepartmentListView,
    DepartmentDetailView,
    DepartmentCreateView,
    DepartmentUpdateView,
)

urlpatterns = [
    url(r'^$', DepartmentListView.as_view(), name='list'),
    url(r'^create/$', DepartmentCreateView.as_view(), name='create'),
    # # slug
    #url(r'^(?P<slug>[\w-]+)/$', DepartmentDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', DepartmentUpdateView.as_view(), name='edit'),
]