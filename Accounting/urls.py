from django.urls import path, include
from . import views

app_name = "Accounting"
urlpatterns = [
    path("signup", views.signup_View, name = "signup"),
    path("signin", views.signin_View, name = "signin"),
    path('logout', views.signout_View, name="signout"),
    path("profile/<str:pk>", views.userProfile, name="userProfile"),
]