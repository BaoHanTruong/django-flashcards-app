from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('topic/<int:topic_id>/', views.flashcards, name='flashcards'),
]