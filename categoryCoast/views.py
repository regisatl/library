from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import  Category
from .forms import CategoryForm


# Vue pour l'index
def index(request):
    active_page = "categories"
    categories = Category.objects.all()  # Récupère tous les catégories disponibles
    return render(request, "categoryCoast/index.html", {"categories": categories, 'active_page': active_page})


# Vue pour afficher une catégorie spécifique
@login_required
def show(request, category_id):
    category = get_object_or_404(Category, pk=category_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    return render(request, "categoryCoast/show.html", {"category": category})


# Vue pour ajouter une nouvelle catégorie
@user_passes_test(lambda u: u.is_superuser)
def add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("categoryCoast:index")
    else:
        form = CategoryForm()
    return render(request, "categoryCoast/add.html", {"form": form})


# Vue pour modifier une catégorie existant
@user_passes_test(lambda u: u.is_superuser)
def edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categoryCoast:show", category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, "categoryCoast/edit.html", {"form": form})

# Vue pour supprimer une catégorie existant
@user_passes_test(lambda u: u.is_superuser)
def remove(request, category_id):
    category = get_object_or_404(Category, pk=category_id)  # Récupère le livre ou renvoie une erreur 404 si non trouvé
    if request.method == "POST":
        category.delete()
        return redirect("categoryCoast:index")
    return render(request, "categoryCoast/remove.html", {"category": category})
