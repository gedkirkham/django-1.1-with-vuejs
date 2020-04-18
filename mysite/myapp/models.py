from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified =  models.DateTimeField(auto_now=True)