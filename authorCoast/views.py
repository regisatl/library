from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Author
from .forms import AuthorForm


# Vue pour l'index
def index(request):
    authors = Author.objects.all()  # Récupère tous les livres disponibles
    return render(request, "authorCoast/index.html", {"authors": authors})


# Vue pour afficher un livre spécifique
def show(request, author_id):
    author = get_object_or_404(Author, pk=author_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    return render(request, "authorCoast/show.html", {"author": author})


# Vue pour ajouter un nouveau livre
def add(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("authorCoast:index")
    else:
        form = AuthorForm()
    return render(request, "authorCoast/add.html", {"form": form})


# Vue pour modifier un livre existant
def edit(request, author_id):
    author = get_object_or_404(Author, pk=author_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect("authorCoast:show", author_id=author.id)
    else:
        form = AuthorForm(instance=author)
    return render(request, "authorCoast/edit.html", {"form": form, 'author': author})


# Vue pour supprimer un livre existant
def remove(request, author_id):
    author = get_object_or_404(Author, pk=author_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        author.delete()
        return redirect("authorCoast:index")
    return render(request, "authorCoast/remove.html", {"author": author})
