from django.urls import path;
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.delete, name="index_delete"),
    path("<int:pk>", views.update, name="index_update"),
]