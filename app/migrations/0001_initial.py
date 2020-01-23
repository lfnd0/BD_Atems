from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoIndicativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao_indicativa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Classificação indicativa',
            },
        ),
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Gêneros',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Locais',
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Local')),
            ],
            options={
                'verbose_name_plural': 'Servidores',
            },
        ),
        migrations.CreateModel(
            name='JogoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_lancamento', models.DateField()),
                ('preco', models.FloatField()),
                ('classificacao_indicativa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ClassificacaoIndicativa')),
                ('distribuidora', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Distribuidora')),
                ('genero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Genero')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Servidor')),
            ],
            options={
                'verbose_name_plural': 'Jogos pagos',
            },
        ),
        migrations.CreateModel(
            name='JogoGratuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_lancamento', models.DateField()),
                ('classificacao_indicativa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ClassificacaoIndicativa')),
                ('distribuidora', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Distribuidora')),
                ('genero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Genero')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Servidor')),
            ],
            options={
                'verbose_name_plural': 'Jogos gratuitos',
            },
        ),
        migrations.AddField(
            model_name='distribuidora',
            name='local',
            field=models.ManyToManyField(to='app.Local'),
        ),
        migrations.AddField(
            model_name='distribuidora',
            name='servidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Servidor'),
        ),
        migrations.AddField(
            model_name='distribuidora',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]