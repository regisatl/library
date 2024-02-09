from django import forms
from .models import Author, Category, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "biography", "image"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["description"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "categories",
            "cover",
            "summary",
            "publish_date",
            "statut",
        ]
