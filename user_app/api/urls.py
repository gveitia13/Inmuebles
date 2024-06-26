from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views

from user_app.api.views import registration_view, logout_view, login_view, session_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('login-app/', login_view, name='login-app'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('session/', session_view, name='session'),

    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
