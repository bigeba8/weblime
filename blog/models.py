from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_summernote.fields import SummernoteTextField
from django.utils.text import slugify
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null=False, default=None)
    cover_image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    content = SummernoteTextField(blank=True, null=True)
    excerpt = models.TextField(null=True, default=None, max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        #super().save()

        img = Image.open(self.cover_image.path)

        if img.height > 450 or img.width > 450:
            output_size = (450, 450)
            img.thumbnail(output_size)
            img.save(self.cover_image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
