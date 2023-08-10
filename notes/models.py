from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    body_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

