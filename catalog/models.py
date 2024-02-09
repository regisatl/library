from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the author name")
    biography = models.TextField(help_text="Enter the author biography")
    image = models.ImageField(
        upload_to="authors/", blank=True, help_text="Upload the author image"
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(
        max_length=255, help_text="Enter the category description"
    )

    def __str__(self):
        return self.description


class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Enter the title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")
    cover = models.ImageField(
        upload_to="covers/", blank=True, help_text="Upload the cover image"
    )
    summary = models.TextField(help_text="Enter a brief description of the book")
    publish_date = models.DateField(
        null=True, blank=True, help_text="Enter the publish date"
    )
    statut = models.BooleanField(default=True, help_text="Availability status")

    def __str__(self):
        return self.title
