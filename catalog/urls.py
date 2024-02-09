from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
      path('', views.index, name='index'), # catalog/
      path('<int:book_id>/', views.show, name='show'), # catalog/<id>
      path('addBook/', views.add, name='add'), # catalog/add
      path('editBook/<int:book_id>/', views.edit, name='edit'), # catalog/edit
      path('deleteBook/<int:book_id>/', views.remove, name='delete'), # catalog/edit
]