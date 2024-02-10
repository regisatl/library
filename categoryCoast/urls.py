from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "categoryCoast"

urlpatterns = [
    path('', views.index, name='index', name='index'),
    path('<int:category_id>/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('edit/<int:category_id>/', views.edit, name='edit'),
    path('remove/<int:category_id>/', views.remove, name='remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)