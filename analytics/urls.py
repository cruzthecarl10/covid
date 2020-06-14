from django.urls import path
from analytics import views

urlpatterns = [
	path('home/', views.home, name='home'),
]