from .forms import ObjectFlatForm
from django.shortcuts import redirect
from .models import ObjectFlat, Table
from django.shortcuts import render, get_object_or_404
from django_pandas.io import read_frame
from .get_price import get_data
from .get_price import get_price


def base_page(request):
    return render(request, 'testtest/base.html', {})

def valuation_result(request, pk):   #передать объект оценки в функцию get_price из файла get_price
    valuation = get_object_or_404(ObjectFlat, pk=pk)
    #df = read_frame(valuation)
    #qs = Table.objects.all()
    #qs = Table.objects.filter(zone = valuation.zone)
    #df = read_frame(qs)
    #prices = df.price

    #df = [valuation.zone, valuation.rooms, valuation.floor, valuation.wall_material, valuation.remont, valuation.lift, valuation.parking]

    #price = get_price(valuation.zone, valuation.rooms, valuation.floor, valuation.wall_material, valuation.remont, valuation.lift, valuation.parking)
    price = get_price('Автозаводский', '1 комната', 'первый этаж', 'нет данных', 'типовой', 'нет данных', 'нет данных')
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