from django.urls import path, include
from . import views

app_name = "Accounting"
urlpatterns = [
    path("signup", views.signup_View, name = "Signup"),
    path("signin", views.signin_View, name = "Signin"),
    path("test", views.test, name = "test")
    # path('login',views.loginForm, name="Login"),
    # path('logout', views.user_logout, name="Logout"),
    # path("profile/<slug:slug>", views.userProfile, name="UserProfile"),
]