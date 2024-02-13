from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'categories', 'cover', 'summary', 'publish_date', 'statut']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Entrez le titre du livre'}),
            'author': forms.Select(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Sélectionnez un auteur pour le livre'}),
            'categories': forms.SelectMultiple(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Sélectionnez une ou plusieurs catégories pour ce livre'}),
            'cover': forms.FileInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Choisissez une image de couverture'}),
            'summary': forms.Textarea(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Entrez un résumé'}),
            'publish_date': forms.DateInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full', 'placeholder': 'Entrez la date de publication'}),
            'statut': forms.CheckboxInput(attrs={'class': 'block mb-2 text-sm font-medium text-gray-600 dark:text-gray-300 bg-white p-2 rounded-lg border border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 w-full'}),
        }