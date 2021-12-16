from django.urls import path
from .views import LoginView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView,UserDetail,UserList
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('users/',UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',UserDetail.as_view(),name='user-detail'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
