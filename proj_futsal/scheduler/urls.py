from django.urls import path
from . import views

app_name = 'scheduler'
urlpatterns = [
    path('home', views.home, name = 'home'),
    path('event/<int:pk>/', views.event, name='event'),
    path('register', views.register, name='register'),
    #path('edit/<int:pk>/', views.editPlayer, name='edit'),
]

print('loaded urls')