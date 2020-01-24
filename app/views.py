from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Local 
from .forms import DistribuidoraForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', { 'form': form })

@login_required
def adicionar_distribuidora(request):
    usuario = request.user

    if request.method == 'POST':
        form = DistribuidoraForm(request.POST)
        if form.is_valid():
            distribuidora = form.save(commit=False)
            distribuidora.usuario = usuario
            distribuidora.save()
            form.save_m2m()
            return redirect('listar_distribuidoras')
    else:
        form = DistribuidoraForm()

    return render(request, 'adicionar_distribuidora.html', {'form': form})

@login_required
def listar_distribuidoras(request):
    return render(request, 'listar_distribuidoras.html')

@login_required
def listar_jogos(request):
    return render(request, 'listar_jogos.html')