from django.conf.urls import url

from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    CourseListView,
    CourseDetailView,
    DepartmentListView,
    DepartmentDetailView,
)

urlpatterns = [

    

    url(r'^$', StudentListView.as_view(), name='list'),
    # url(r'^restaurant/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurant/(?P<res_id>\w+)/$', RestaurantDetailView.as_view()),
    # url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^create/$', StudentCreateView.as_view(), name='create'),
    # slug
    url(r'^(?P<slug>[\w-]+)/$', StudentDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='edit'),
    # url(r'^restaurant/mexican/$', MexicanRestaurantListView.as_view()),
    # url(r'^restaurant/asian/$', AsianFusionRestaurantListView.as_view()),
]