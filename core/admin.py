from django.contrib import admin
from . import models, forms

@admin.register(models.SMDManager)
class AdminSMDManager(admin.ModelAdmin):
    list_display = ( 'cognome', 'nome', 'ore')

@admin.register(models.Turno)
class AdminTurno(admin.ModelAdmin):
    list_display = ('dip','giorno', 'inizio', 'fine', 'durata')
    ordering = ('-giorno',)
    form = forms.TurnoForm

