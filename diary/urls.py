from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.diary_new),
    path('<int:pk>/', views.memory_detail),
    path('', views.index),
]