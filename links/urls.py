from django.contrib import admin
from django.urls import path
from .views import index, new, root_link

urlpatterns = [
    path("", index, name="home"),
    path('<str:link_slug>/', root_link, name="root-link"),
    path("link/create/", new, name="create_link"),
]
