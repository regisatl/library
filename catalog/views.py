from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Category
from .forms import BookForm, AuthorForm, CategoryForm


# Vue pour l'index
def index(request):
    books = Book.objects.filter(statut=True)  # Récupère tous les livres disponibles
    return render(request, "index.html", {"books": books})


# Vue pour afficher un livre spécifique
def show(request, book_id):
    book = get_object_or_404(
        Book, pk=book_id
    )  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    return render(request, "show.html", {"book": book})


# Vue pour ajouter un nouveau livre
def add(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm()
    return render(request, "add.html", {"form": form})


# Vue pour modifier un livre existant
def edit(request, book_id):
    book = get_object_or_404(
        Book, pk=book_id
    )  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("show", book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "edit.html", {"form": form})


# Vue pour supprimer un livre existant
def remove(request, book_id):
    book = get_object_or_404(
        Book, pk=book_id
    )  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        book.delete()
        return redirect("index")
    return render(request, "remove.html", {"book": book})
