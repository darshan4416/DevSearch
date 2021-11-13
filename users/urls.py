
from django.urls import path, include
from .views import profiles, registerUser,user_profile, loginPage, logoutPage

urlpatterns = [
    
    path('',profiles,name="profiles"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('register/', registerUser, name="register"),
    path('user_profile/<str:pk>/',user_profile, name="user_profile")
]

