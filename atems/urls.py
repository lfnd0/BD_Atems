from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('atems/distribuidoras/', views.listar_distribuidoras, name='listar_distribuidoras'),
    path('atems/adicionar/distribuidora', views.adicionar_distribuidora, name='adicionar_distribuidora'),
    path('atems/distribuidora/jogos', views.listar_jogos, name='listar_jogos'),
]