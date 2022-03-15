from django.urls import path, include
from .views import UserView, UserDetailView, UserLoginView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),

    path('users/', UserView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),

    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('webpush/', include('webpush.urls'))
]
