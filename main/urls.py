from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('blog.urls')),
    path('who-we-are/', views.who_we_are, name='who-we-are'),
    path('solutions/', views.solutions, name='solutions'),
    path('get-in-touch/', views.get_in_touch, name='get-in-touch'),
]
