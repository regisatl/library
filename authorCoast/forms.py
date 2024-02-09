from django import forms
from catalog.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "biography", "image"]


