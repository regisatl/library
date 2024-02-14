from django import forms
from catalog.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["description"]
        widgets = {
            'description': forms.TextInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Entrez la description du livre'}),
        }
