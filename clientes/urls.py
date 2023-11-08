from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path("/post/<int:cliente_id>", views.cliente, name="post"),
]