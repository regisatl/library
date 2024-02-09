from django import forms
from .models import Book, Author, Category


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


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "biography"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["description"]
