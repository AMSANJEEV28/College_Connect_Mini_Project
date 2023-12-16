# social/urls.py
from django.urls import path
from .views import create_group, search_group, join_group, group_detail
from .views import feeds_view


urlpatterns = [
    path('create_group/', create_group, name='create_group'),
    path('search_group/', search_group, name='search_group'),
    path('join_group/<str:group_id>/', join_group, name='join_group'),
    path('group_detail/<str:group_id>/', group_detail, name='group_detail'),
    path('feeds/', feeds_view, name='feeds'),

    # Add other URLs as needed
]
