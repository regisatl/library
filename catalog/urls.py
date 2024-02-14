from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('edit/<int:book_id>/', views.edit, name='edit'),
    path('remove/<int:book_id>/', views.remove, name='remove'),
    path('search/', views.book_search, name='book_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)