from .forms import ObjectFlatForm
from django.shortcuts import redirect
from .models import ObjectFlat
    # , Table
from django.shortcuts import render, get_object_or_404
#from django_pandas.io import read_frame
#from .get_price import get_av_price


def base_page(request):
    return render(request, 'testtest/base.html', {})

def valuation_result(request, pk):
    valuation = get_object_or_404(ObjectFlat, pk=pk)

    #qs = Table.objects.all()
    #qs = Table.objects.filter(zone = valuation.zone)
    #df = read_frame(qs)
    #prices = df.price
    #price = get_av_price(prices)

    #object_val = {'Район': df.zone, 'Комнат': df.rooms,  'Этаж': df.floor,
                  #'Материал стен': df.wall_material, 'Ремонт': df.remont, 'Парковка': df.parking, 'Лифт': df.lift}


    price = 15*3
    #return render(request, 'testtest/valuation_result.html', {'price': price})
    return render(request, 'testtest/valuation_result.html', {'df': price})


def valuation_new(request):
    if request.method == 'POST':
        form = ObjectFlatForm(request.POST)
        valuation = form.save(commit=False)
        valuation.save()
        return redirect('valuation_result', pk=valuation.pk)
    else:
        form = ObjectFlatForm()
    return render(request, 'testtest/fill_form.html', {'form': form})