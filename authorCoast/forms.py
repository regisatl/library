from django import forms
from catalog.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "biography", "image"]
        widgets = {
                    'name': forms.TextInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Entrez le nom de l\'auteur'}),
                    'biography': forms.Textarea(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Entrez la biographie de l\'auteur'}),
                    'image': forms.FileInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Choissez une image'}),
                }