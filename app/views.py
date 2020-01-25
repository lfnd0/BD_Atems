from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse
from django.utils.decorators import method_decorator

from .models import Distribuidora, JogoGratuito, JogoPago
from .forms import DistribuidoraForm, JogoGratuitoForm, JogoPagoForm, DistribuidoraUpdateForm

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
def listar_distribuidoras(request):
    usuario = request.user.id
    distribuidoras = Distribuidora.objects.filter(usuario__pk=usuario)
    return render(request, 'listar_distribuidoras.html', { 'distribuidoras': distribuidoras })

@method_decorator([login_required], name='dispatch')
class DistribuidoraUpdateView(UpdateView):
    model = Distribuidora
    form_class = DistribuidoraUpdateForm
    template_name = 'atualizar_distribuidora_form.html'

    def get_success_url(self):
        return reverse('listar_distribuidoras')

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
def apagar_distribuidora(request, id):
    distribuidora = get_object_or_404(Distribuidora, pk=id)
    distribuidora.delete()
    return redirect('listar_distribuidoras')

@login_required
def listar_jogos_distribuidora(request, pk):
    jogos_gratuitos = JogoGratuito.objects.filter(distribuidora__pk=pk)
    jogos_pagos = JogoPago.objects.filter(distribuidora__pk=pk)
    return render(request, 'listar_jogos_distribuidora.html', {'jogos_gratuitos': jogos_gratuitos, 'jogos_pagos': jogos_pagos})

@login_required
def listar_jogos(request):
    usuario = request.user.id
    jogos_gratuitos = JogoGratuito.objects.filter(usuario__pk=usuario)
    jogos_pagos = JogoPago.objects.filter(usuario__pk=usuario)
    return render(request, 'listar_jogos.html', {'jogos_gratuitos': jogos_gratuitos, 'jogos_pagos': jogos_pagos })

@login_required
def adicionar_jogo_gratuito(request, pk):
    usuario = request.user
    distribuidora = get_object_or_404(Distribuidora, pk=pk)

    if request.method == 'POST':
        form = JogoGratuitoForm(request.POST)
        if form.is_valid():
            jogo_gratuito = form.save(commit=False)
            jogo_gratuito.usuario = usuario
            jogo_gratuito.distribuidora = distribuidora
            jogo_gratuito.save()
            return redirect('listar_jogos_distribuidora', distribuidora.pk)
    else:
        form = JogoGratuitoForm()
    return render(request, 'adicionar_jogo_gratuito.html', { 'distribuidora': distribuidora, 'form': form })

@method_decorator([login_required], name='dispatch')
class JogoGratuitoUpdateView(UpdateView):
    model = JogoGratuito
    fields = ['nome', 'distribuidora', 'genero', 'classificacao_indicativa']
    template_name = 'atualizar_gratuito_form.html'

    def get_success_url(self):
        return reverse('listar_jogos')

@method_decorator([login_required], name='dispatch')
class JogoPagoUpdateView(UpdateView):
    model = JogoPago
    fields = ['nome', 'distribuidora', 'genero', 'classificacao_indicativa', 'preco']
    template_name = 'atualizar_jogo_pago_form.html'

    def get_success_url(self):
        return reverse('listar_jogos')

@login_required
def adicionar_jogo_pago(request, pk):
    usuario = request.user
    distribuidora = get_object_or_404(Distribuidora, pk=pk)

    if request.method == 'POST':
        form = JogoPagoForm(request.POST)
        if form.is_valid():
            jogo_pago = form.save(commit=False)
            jogo_pago.usuario = usuario
            jogo_pago.distribuidora = distribuidora
            jogo_pago.save()
            return redirect('listar_jogos_distribuidora', distribuidora.pk)
    else:
        form = JogoPagoForm()
    return render(request, 'adicionar_jogo_pago.html', { 'distribuidora': distribuidora, 'form': form })

@login_required
def apagar_jogo_gratuito(request, id):
    jogo_gratuito = get_object_or_404(JogoGratuito, pk=id)
    jogo_gratuito.delete()
    return redirect('listar_jogos')

@login_required
def apagar_jogo_pago(request, id):
    jogo_pago = get_object_or_404(JogoPago, pk=id)
    jogo_pago.delete()
    return redirect('listar_jogos')
