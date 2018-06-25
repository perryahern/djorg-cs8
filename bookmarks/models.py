from django.db import models
from uuid import uuid4

# Create your models here.

class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  url = models.URLField(max_length=200)
  note = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)