from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('foryou/', api.foryou, name='foryou'),
    path('signup/', api.signup, name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('friends/request/<uuid:pk>',
         api.send_friend_request, name='send_friend_request'),
    path('profile/<uuid:pk>/friends/', api.friends, name='friends'),
    path('friends/<uuid:pk>/<str:status>',
         api.handle_friend_request, name='handle_friend_request')
]
