from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile_home, name='profile'),
    path('user_posts/', views.user_posts, name='user-posts'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/<int:user_id>', views.PostDetailViewUser.as_view(), name='post-detail-user'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('blogpost/new/', views.PostCreateView.as_view(), name='post-create'),
]
