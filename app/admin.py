from django.contrib import admin

from .models import Local, Distribuidora, ClassificacaoIndicativa, Genero, JogoGratuito, JogoPago

admin.site.register(Local)
admin.site.register(Distribuidora)
admin.site.register(ClassificacaoIndicativa)
admin.site.register(Genero)
admin.site.register(JogoGratuito)
admin.site.register(JogoPago)