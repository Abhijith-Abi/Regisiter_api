from django.urls import path
from api.v1.register import views


urlpatterns = [
    path('', views.register),
]
