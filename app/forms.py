from django import forms

from .models import Local, Distribuidora, Genero, ClassificacaoIndicativa, JogoGratuito, JogoPago

class DistribuidoraForm(forms.ModelForm):
    local = forms.ModelMultipleChoiceField(
        queryset=Local.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Distribuidora
        fields = ('nome', 'local', )

class JogoGratuitoForm(forms.ModelForm):
    class Meta:
        model = JogoGratuito
        fields = ('nome', 'data_lancamento', 'genero', 'classificacao_indicativa', )

class JogoPagoForm(forms.ModelForm):
    class Meta:
        model = JogoPago
        fields = ('nome', 'data_lancamento', 'genero', 'classificacao_indicativa', 'preco', )

class DistribuidoraUpdateForm(forms.ModelForm):
    local = forms.ModelMultipleChoiceField(
        queryset=Local.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Distribuidora
        fields = ('nome', 'local', )