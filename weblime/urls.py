from django.contrib import admin
from django.urls import path, include
from main import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('settings/', user_views.settings, name='settings'),
    path('blog', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
