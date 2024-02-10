from django.urls import path
from . import views

app_name = "authorCoast"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:author_id>/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('edit/<int:author_id>/', views.edit, name='edit'),
    path('remove/<int:author_id>/', views.remove, name='remove'),
]

