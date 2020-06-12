from django.urls import path
from filesAndFolders import views

url_patterns = [
    path('', views.Hompage.as_view(), name='homepage')
]
