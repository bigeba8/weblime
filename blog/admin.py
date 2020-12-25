from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'excerpt', 'author', 'date_posted')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
