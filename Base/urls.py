from django.urls import path
from . import views

app_name = "Base"
urlpatterns = [
    path("", views.showHome, name="home"),
    path("sidebar", views.sidebar, name="sidebar")
]
