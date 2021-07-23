from django.shortcuts import render, redirect
from .forms import *


def main(request):
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Request()
    return render(request, 'main/main.html', {'form': form})
