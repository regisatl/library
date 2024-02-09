from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, help_text='Enter the title')
    author = models.CharField(max_length=255, help_text='Enter the author name')
    summary = models.TextField(help_text='Enter a brief description of the book')
    cover = models.ImageField(upload_to='covers/', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text='Enter the price of the book')
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
      return self.title
