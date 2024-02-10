from django import forms
from catalog.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["description"]


