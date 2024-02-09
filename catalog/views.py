from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Category
from .forms import BookForm, AuthorForm, CategoryForm


def index(request):
    books = Book.objects.filter(
        is_available=True
    )  # Récupère tous les livres disponibles
    return render(request, "index.html", {"books": books})


# Vue pour créer un nouveau livre
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm()
    return render(request, "create_book.html", {"form": form})


# Vue pour lire les détails d'un livre spécifique
def read_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "read_book.html", {"book": book})


# Vue pour mettre à jour un livre existant
def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("read_book", book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "update_book.html", {"form": form})


# Vue pour supprimer un livre existant
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("index")
    return render(request, "delete_book.html", {"book": book})
