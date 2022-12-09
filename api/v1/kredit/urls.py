from django.urls import path
from .views import  *


urlpatterns = [
    path('create-credit', create_credit_view, name='create-credit'),
    path('view-my-credit', view_my_credit, name='view my credits'),
    path('update-credit/<int:pk>', update_credit_view, name='update-credit'),
    path('delete-my-credit', delete_credit_view, name='delete-credit'),
    ]
