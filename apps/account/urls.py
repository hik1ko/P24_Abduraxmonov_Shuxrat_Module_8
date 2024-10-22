from django.urls import path

from apps.account.views import UserView

urlpatterns = [
    path('user/', UserView.as_view({'get': 'list'}), name='user'),
]