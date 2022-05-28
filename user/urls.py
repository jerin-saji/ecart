from django.urls import path,include

from user.views import DashboardView, LoginView, LogoutView, ProfileCreateView, UserRegistrationView, ProfileView

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/create', ProfileCreateView.as_view(), name='profile_create'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]