from .forms import ObjectFlatForm
from django.shortcuts import redirect
from .models import ObjectFlat
from django.shortcuts import render, get_object_or_404



def base_page(request):
    return render(request, 'testtest/base.html', {})

def valuation_result(request, pk):
    valuation = get_object_or_404(ObjectFlat, pk=pk)
    price = 15*3
    return render(request, 'testtest/valuation_result.html', {'price': price})


def valuation_new(request):
    if request.method == 'POST':
        form = ObjectFlatForm(request.POST)
        valuation = form.save(commit=False)
        valuation.save()
        return redirect('valuation_result', pk=valuation.pk)
    else:
        form = ObjectFlatForm()
    return render(request, 'testtest/fill_form.html', {'form': form})




