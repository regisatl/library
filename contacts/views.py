from django.shortcuts import render, redirect
from .models import Contact  # Assurez-vous d'importer le modèle Contact
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "contacts:index"
            )  # Remplacez 'success_url' par l'URL de votre choix
    else:
        form = ContactForm()

    # Récupérer tous les contacts de la base de données
    contacts = Contact.objects.all()

    return render(request, "contacts/index.html", {"form": form, "contacts": contacts})
