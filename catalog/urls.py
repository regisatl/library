from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "catalog"

urlpatterns = [
    path('', views.index, name='index'),  # Vue pour l'index
    path('<int:book_id>/', views.read_book, name='read_book'),  # Vue pour lire un livre spécifique
    path('add/', views.create_book, name='create_book'),  # Vue pour ajouter un nouveau livre
    path('edit/<int:book_id>/', views.update_book, name='update_book'),  # Vue pour modifier un livre existant
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Vue pour supprimer un livre existant
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)