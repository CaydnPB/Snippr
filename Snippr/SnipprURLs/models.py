from django.db import models
from django.utils import timezone

class SnipprSnippet(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    code = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Snippr Snippet'
        verbose_name_plural = 'Snippr Snippets'