from django.urls import path
from api.v1.ad.views import *

app_name = 'ad'

urlpatterns = [
    path('update-ad/<int:pk>', update_ad, name='update-ad'),
    path('delete-ad/<int:pk>', delete_ad, name='delete-ad'),
    path('get-ad/<int:pk>', get_ad, name='get-ad'),
    path('get-ads/', ads_view, name='get-ads'),
    path('get-my-ads/', my_ads_view, name='get-ads'),
    path('search/', search_view, name='search'),
    path('ordering/', AdListFilterView.as_view(), name='filter'),
    path('create-ad/', create_ad, name='create-ad'),
    path('get-subcategories-view/', get_subcategories_view),
    path('get-categories-view/', get_categories_view),

    path('fav-ad/', get_fav_ad_view),
    path('fav-ad/<int:pk>', get_fav_ad_retrieve_view),
    path('fav-ad-create/', create_fav_ad_view),
    path('fav-ad-update/<int:pk>', update_fav_ad_view),
    path('fav-ad-delete/<int:pk>', delete_fav_ad_view),

    path('post-viewed-ad/<int:pk>', post_viewed_ad),

    path('get-location-ad/<int:pk>', get_ad_location_view),
    path('delete-location-ad/<int:pk>', delete_ad_location_view),
    path('ad-location-post/', create_ad_location_view),

    path('get-picture-ad/<int:pk>', get_ad_picture_view),
    path('delete-picture-ad/<int:pk>', delete_ad_picture_view),
    path('ad-picture-post/', create_ad_picture_view),

]
