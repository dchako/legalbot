from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view(), name='post_register'),
    path('login', LoginView.as_view(),  name='post_login'),
    path('userProfile', UserView.as_view(), name='get_userprofile'),
    path('logout', LogoutView.as_view(), name='post_logout'),
]
