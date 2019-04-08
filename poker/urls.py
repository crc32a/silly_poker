from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="index"),
    path("test", views.test, name="test_page")
]