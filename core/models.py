from django.db import models
from django.core.serializers import serialize
from django.http import JsonResponse
class SMDManager(models.Model):
    nome = models.CharField(verbose_name='nome manager', max_length=255)
    cognome = models.CharField(verbose_name='cognome manager', max_length=255)
    ore = models.PositiveSmallIntegerField(verbose_name='ore settimanale', default=40)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.cognome)


class Turno(models.Model):
    dip = models.ForeignKey(SMDManager,on_delete=models.CASCADE, related_name='turni')
    giorno = models.DateField()
    inizio = models.DateTimeField()
    fine = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turni"

    def durata(self):
        return self.fine - self.inizio

    def durata_ore(self):
        return int(self.durata().total_seconds() / 3600)

    def durata_minuti(self):
        return int((self.durata().total_seconds() % 3600) / 60)
    def orario(self):
        return (self.inizio.strftime("%H:%M"), self.fine.strftime("%H:%M"))
    def __str__(self):
        init = self.inizio.strftime("%H:%M")
        fine = self.fine.strftime("%H:%M")
        return '%s - %s -[%s <--> %s ] %s : %s ' % (self.dip, self.giorno, init , fine, self.durata_ore(), self.durata_minuti())

