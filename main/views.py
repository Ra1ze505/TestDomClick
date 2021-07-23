from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import *
from .models import UserRequest


def main(request):
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            try:
                UserRequest.objects.create(name=cd['name'], email=cd['email'])
            except IntegrityError:
                pass
            return redirect('/')
    else:
        form = Request()
    return render(request, 'main/main.html', {'form': form})
