from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepageviews),
    path("details", views.details, name="details"),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete),
]
