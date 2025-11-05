from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'), # Login page route
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),  # Home page route
    path('room/<str:pk>/', views.room, name='room'),  # Room page route
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),  # User profile route
    path('create-room/', views.createRoom, name='create-room'),  # Create room route
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),  # Update room route
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
]