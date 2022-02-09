from django.db import models
from django.conf import settings
from django.utils.text import slugify
import time
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Forum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.title) + '-' + time.strftime("%Y%m%d%H%M%S")
        super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('forum-detail', kwargs={'slug': self.slug})

    # def get_nomber_comment(self):
    #     nbr_comment = Comment.objects.get

	
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('forum-detail', kwargs={'slug': self.slug})

	