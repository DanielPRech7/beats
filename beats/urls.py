from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importa as views de autenticação


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('accounts/', include('beats.accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('beats.playlist.urls')),

]