# Generated by Django 3.0.3 on 2020-03-13 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=40, verbose_name='Sigla')),
                ('data_inicio', models.DateField(verbose_name='Data Inicio')),
                ('descrição', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrição', models.CharField(max_length=40, verbose_name='Descrição')),
                ('valor', models.FloatField(max_length=40, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_ingresso.Pessoa')),
            ],
            bases=('app_ingresso.pessoa',),
        ),
        migrations.CreateModel(
            name='Inscrição',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ingresso.Evento', verbose_name='Evento')),
                ('ingresso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ingresso.Ingresso', verbose_name='Ingresso')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ingresso.Pessoa', verbose_name='Pessoa')),
            ],
        ),
    ]
