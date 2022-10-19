from django.urls import path
from api.v1.register import views


urlpatterns = [
    path('', views.register),
    path('view/<int:pk>/', views.register_list),
    path('create/', views.create_data),
    path('update/<int:pk>/', views.update_data),
    path('delete/<int:pk>/', views.delete_data),
]
