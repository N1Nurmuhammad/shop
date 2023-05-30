from django.urls import path
from api.v1.ad.views import *

app_name = 'ad'

urlpatterns = [
    path('update-ad/<int:pk>', update_ad, name='update-ad'),
    path('delete-ad/<int:pk>', delete_ad, name='delete-ad'),
    path('get-ad/<int:pk>', get_ad, name='get-ad'),
    path('get-ads/', ads_view, name='get-ads'),
    path('search/', search_view, name='search'),
    path('ordering/', AdListFilterView.as_view(), name='filter'),

    path('create-ad/', create_ad, name='create-ad'),




]