from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  url = models.URLField(max_length=200)
  note = models.TextField()
  category = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class PrivateBookmark(Bookmark):
  user = models.ForeignKey(User, on_delete=models.CASCADE)