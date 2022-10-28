from django.urls import path
from diary import views


urlpatterns = [
    path('new/', views.memory_new),
    path('<int:pk>/', views.memory_detail),
    path('', views.memory_list),
]