from django.contrib import admin
from django.urls import path, include   # ← importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')),   # ← incluye las URLs de la app gestion
]