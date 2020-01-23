from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('atems/distribuidoras/', views.distribuidoras, name='distribuidoras'),
    path('atems/distribuidora/jogos', views.jogos, name='jogos')
]