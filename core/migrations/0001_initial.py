# Generated by Django 5.0.6 on 2024-06-10 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMDManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome manager')),
                ('cognome', models.CharField(max_length=255, verbose_name='cognome manager')),
                ('ore', models.PositiveSmallIntegerField(default=40, verbose_name='ore settimanale')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giorno', models.DateField()),
                ('inizio', models.DateTimeField()),
                ('fine', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turni', to='core.smdmanager')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turni',
            },
        ),
    ]
