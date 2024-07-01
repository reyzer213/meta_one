from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['author']
        indexes = [models.Index(fields=['isbn']),]

    def __str__(self):
        return self.title