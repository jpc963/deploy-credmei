# Generated by Django 4.2.1 on 2023-06-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoCep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField()),
                ('estado', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=30)),
                ('rua', models.CharField(max_length=30)),
                ('servico', models.CharField(max_length=15)),
            ],
        ),
    ]
