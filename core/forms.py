from django import forms
from . import models
from django.db.models import Q
from datetime import timedelta
class TurnoForm(forms.ModelForm):
    class Meta:
        model = models.Turno
        fields = ('dip', 'giorno', 'inizio', 'fine')


    def clean_fine(self):
        giorno = self.cleaned_data.get('giorno')
        fine = self.cleaned_data.get('fine')
        inizio = self.cleaned_data.get('inizio')
        if fine.date() < giorno:
            raise forms.ValidationError('la fine deve essere piu grande di %s' % giorno)
        if fine <= inizio:
            raise forms.ValidationError('la fine deve essere pi grande di %s ' % inizio)
        return fine

    def clean_inizio(self):

        inizio = self.cleaned_data.get('inizio')
        giorno = self.cleaned_data.get('giorno')

        if inizio.date() < giorno:
            raise forms.ValidationError('%s deve essere piu grande di %s' % (inizio, giorno))

        return inizio


    def clean(self):
        clean_data = self.cleaned_data
        giorno=clean_data.get('giorno')
        inizio=clean_data.get('inizio')
        fine=clean_data.get('fine')
        dip = clean_data.get('dip')
        """ controlla se esiste gia un turno con le stese ore """
        turni  = models.Turno.objects.all().filter(dip=dip, giorno=giorno
        ).exclude(id=self.instance.pk)
        if turni:
            for turno in turni:
                if inizio >= turno.inizio and inizio < turno.fine:
                    raise forms.ValidationError('esiste gia un turno [%s %s] che contiene %s' % (turno.inizio.strftime("%H:%M"),turno.fine.strftime("%H:%M"),inizio.strftime("%H:%M")))
                if fine > turno.inizio and fine <= turno.fine:
                    raise forms.ValidationError('esiste gia un turno [%s %s] che contiene %s' % (turno.inizio.strftime("%H:%M"),turno.fine.strftime("%H:%M"),fine.strftime("%H:%M")))

        """---------fine-----------"""

        """ check se tra l'ultimo turno passano 11 o 35 ore """
        ieri = giorno - timedelta(days=1)
        laltroieri = ieri - timedelta(days=1)
        turno_ieri_q = models.Turno.objects.filter(giorno=ieri, dip=dip).order_by('-fine')
        if turno_ieri_q:
            turno_ieri = turno_ieri_q[0]
            minimo =timedelta(hours=11)
            if inizio - turno_ieri.fine < minimo:
                raise forms.ValidationError('non passano le 11 ore con il turno %s' % turno_ieri)
        else:
            turno_ieri_q = models.Turno.objects.filter(giorno=laltroieri, dip=dip).order_by('-fine')
            if turno_ieri_q:
                turno_ieri = turno_ieri_q[0]
                minimo = timedelta(hours=35)
                if inizio - turno_ieri.fine < minimo:
                    raise forms.ValidationError('non passano le 35 ore con il turno %s' % turno_ieri)
        """---------fine-----------"""

        """check se tra la fine del turno e l'inizio del prossimo passano 11 o 35 ore """
        domani = giorno + timedelta(days=1)
        turno_domani_q = models.Turno.objects.filter(giorno=domani, dip=dip).order_by('inizio')
        if turno_domani_q:
            turno_domani = turno_domani_q[0]
            minimo = timedelta(hours=11)
            if turno_domani.inizio - fine < minimo:
                raise forms.ValidationError('non passano le 11 ore con il turno %s' % turno_domani)
        else:
            dopodomani = domani + timedelta(days=1)
            turno_dopodomani_q = models.Turno.objects.filter(giorno=dopodomani, dip=dip).order_by('inizio')
            if turno_dopodomani_q:
                turno_dopodomani = turno_dopodomani_q[0]
                minimo = timedelta(hours=35)
                if turno_dopodomani.inizio - fine < minimo:
                    raise forms.ValidationError('non passano le 35 ore con il turno %s' % turno_dopodomani)

        return clean_data




