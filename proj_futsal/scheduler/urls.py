from django.urls import path
from . import views

app_name = 'scheduler'
urlpatterns = [
    path('home', views.home, name = 'home'),
    path('event/<int:pk>/', views.event, name='event'),
    path('register', views.register, name='register'),
    path('edit/<int:pk>/', views.EditPlayer.as_view(), name='edit'),
	path('delete/<int:pk>/', views.DeletePlayer.as_view(), name='delete'),
]

print('loaded urls')