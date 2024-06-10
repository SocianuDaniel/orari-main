from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
import datetime
from core import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
# Create your views here.
days = [
    (0, _("Monday")), (1, _("Tuesday")), (2, _("Wednesday")),
    (3, _("Thursday")), (4, _("Friday")), (5, _("Saturday")),
    (6, _("Sunday"))
]
class ListTurni(ListView):
    model = models.Turno
    template_name = 'home/index.html'
    ordering = '-giorno'
    context_object_name = 'turni'
    date_field = 'giorno'

    def get_queryset(self):
        data = datetime.date.today()
        if 'data' in self.kwargs:
            try:
                data = datetime.datetime.strptime(self.kwargs['data'], "%Y-%m-%d")
            except (ValueError, TypeError):
                pass


        lunedi = data - datetime.timedelta(days=data.weekday() % 7)

        domenica = lunedi + datetime.timedelta(days=6)
        querry =models.Turno.objects.all().filter(Q(giorno__range=[lunedi,domenica])).order_by('giorno','inizio')
        orari = {}
        for numar, zi in days:
            orari[zi] = [i for i in querry if i.giorno.weekday() == numar]
        return orari

    def get_context_data(self, **kwargs):
        context = super(ListTurni, self).get_context_data(**kwargs)
        data = datetime.date.today()
        if 'data' in self.kwargs:
            try:
                data = datetime.datetime.strptime(self.kwargs['data'], "%Y-%m-%d")
            except (ValueError, TypeError):
                pass

        lunedi = data - datetime.timedelta(days=data.weekday() % 7)
        prossimo = lunedi + datetime.timedelta(days=7)
        anteriore = lunedi - datetime.timedelta(days=7)
        print(type(prossimo))
        print(anteriore)
        context['anteriore'] = anteriore.strftime("%Y-%m-%d")
        context['prossimo'] = prossimo.strftime("%Y-%m-%d")
        return context

