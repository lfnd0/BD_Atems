from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('atems/distribuidoras/', views.listar_distribuidoras, name='listar_distribuidoras'),
    path('atems/adicionar/distribuidora/', views.adicionar_distribuidora, name='adicionar_distribuidora'),
    path('atems/atualizar/distribuidora/<int:pk>/', views.DistribuidoraUpdateView.as_view(), name='atualizar_distribuidora'),
    path('atems/apagar/distribuidora/<int:id>/', views.apagar_distribuidora, name='apagar_distribuidora'),
    path('atems/distribuidora/<int:pk>/listar/jogos/', views.listar_jogos_distribuidora, name='listar_jogos_distribuidora'),
    
    path('atems/jogos/', views.listar_jogos, name='listar_jogos'),
    
    # path('atems/distribuidora/<int:pk>/adicionar/jogo_gratuito/', views.adicionar_jogo_gratuito, name='adicionar_jogo_gratuito'),
    path('atems/distribuidora/adicionar/jogo_gratuito/', views.adicionar_jogo_gratuito, name='adicionar_jogo_gratuito'),
    path('atems/distribuidora/atualizar/jogo_gratuito/<int:pk>/', views.JogoGratuitoUpdateView.as_view(), name='atualizar_jogo_gratuito'),
    path('atems/distribuidora/apagar/jogo_gratuito/<int:id>/', views.apagar_jogo_gratuito, name='apagar_jogo_gratuito'),
    
    # path('atems/distribuidora/<int:pk>/adicionar/jogo_pago/', views.adicionar_jogo_pago, name='adicionar_jogo_pago'),
    path('atems/distribuidora/adicionar/jogo_pago/', views.adicionar_jogo_pago, name='adicionar_jogo_pago'),
    path('atems/distribuidora/atualizar/jogo_pago/<int:pk>/', views.JogoPagoUpdateView.as_view(), name='atualizar_jogo_pago'),
    path('atems/distribuidora/apagar/jogo_pago/<int:id>/', views.apagar_jogo_pago, name='apagar_jogo_pago'),
]