from django.shortcuts import render
from .models import Object
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def post_list(request):
    return render(request, 'evaluation/post_list.html', {})

def post_new(request):
    a = 15;

    return render(request, 'evaluation/result.html', {'a':a})
