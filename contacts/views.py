from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:index")  # Remplacez 'success_url' par l'URL de votre choix
    else:
        form = ContactForm()
    return render(request, "contacts/index.html", {"form": form})
