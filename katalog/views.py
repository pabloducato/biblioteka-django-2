from django.shortcuts import render

# Create your views here.

from .models import Autor, Gatunek, Ksiazka, InstancjaKsiazki

def index(request):

    num_ks=Ksiazka.objects.all().count() # liczba ksiazek
    num_in=InstancjaKsiazki.objects.all().count() # liczba instancji
    num_in_d=InstancjaKsiazki.objects.filter(status__exact='d').count() # dostepne mialy 'd'
    num_au=Autor.objects.count() # 'all()' nie jest potrzebne, na gorze takze

    # wyswietlamy wszystko w index.html
    return render(
        request,
        'index.html',
        context={'num_ks':num_ks,'num_in':num_in,'num_in_d':num_in_d,'num_au':num_au},
    )



from django.views import generic


class AutorListView(generic.ListView):
    model = Autor
#tutaj template musi nazywac sie autor_list.html
#autor_list to lista autorow domyslnie dostepna

class KsiazkaListView(generic.ListView):
    model = Ksiazka
    context_object_name = 'moja_ksiazka_list'   #moja wlasna zmienna w template, modyfikuje generic
    queryset = Ksiazka.objects.filter(tytul__icontains=' ')[:5]
    template_name = 'katalog/ksiazka_moja_list.html'
    paginate_by = 3

class KsiazkaSzczegolView(generic.DetailView):
    model = Ksiazka
