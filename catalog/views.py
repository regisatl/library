from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


# Vue pour l'index
def index(request):
    active_page = "home"
    books = Book.objects.all().order_by('-publish_date')  # Récupère tous les livres disponibles
    return render(request, "catalog/index.html", {"books": books, 'active_page': active_page})


# Vue pour afficher un livre spécifique
@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    return render(request, "catalog/show.html", {"book": book})


# Vue pour ajouter un nouveau livre
@user_passes_test(lambda u: u.is_superuser)
def add(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalog:index")
    else:
        form = BookForm()
        
    books = Book.objects.all()
    return render(request, "catalog/add.html", {"form": form, "books": books})


# Vue pour modifier un livre existant
@user_passes_test(lambda u: u.is_superuser)
def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("catalog:show", book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "catalog/edit.html", {"form": form, 'book': book})


# Vue pour supprimer un livre 
@user_passes_test(lambda u: u.is_superuser)
def remove(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        book.delete()
        return redirect("catalog:index")
    return render(request, "catalog/remove.html", {"book": book})
