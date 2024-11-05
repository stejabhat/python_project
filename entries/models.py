from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Untitled Entry")
    content = models.TextField(default="No content available.")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True, default="General")
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='story\journal\media\profile_pictures\default-profile.jpg')
