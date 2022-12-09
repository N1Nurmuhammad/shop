from django.urls import path, include

urlpatterns = [
    path('accounts/', include('api.v1.account.urls')),
    path('ad/', include('api.v1.ad.urls')),
    path('credit/', include('api.v1.kredit.urls')),
    path('wallet/', include('api.v1.wallet.urls')),
]