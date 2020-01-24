from django.db import migrations

def create_locais_generos_classificacao_indicativa(apps, schema_editor):
    Local = apps.get_model('app', 'Local')
    Local.objects.create(nome='América do norte')
    Local.objects.create(nome='América do sul')
    Local.objects.create(nome='Europa')
    Local.objects.create(nome='África')
    Local.objects.create(nome='Ásia')
    Local.objects.create(nome='Oceania')

    Genero = apps.get_model('app', 'Genero')
    Genero.objects.create(nome='Ação')
    Genero.objects.create(nome='Aventura')
    Genero.objects.create(nome='Estratégia')
    Genero.objects.create(nome='RPG')
    Genero.objects.create(nome='Esporte')
    Genero.objects.create(nome='Corrida')
    Genero.objects.create(nome='Simulação')

    ClassificacaoIndicativa = apps.get_model('app', 'ClassificacaoIndicativa')
    ClassificacaoIndicativa.objects.create(nome='Livre')
    ClassificacaoIndicativa.objects.create(nome='10')
    ClassificacaoIndicativa.objects.create(nome='12')
    ClassificacaoIndicativa.objects.create(nome='14')
    ClassificacaoIndicativa.objects.create(nome='16')
    ClassificacaoIndicativa.objects.create(nome='18')

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_locais_generos_classificacao_indicativa),
    ]