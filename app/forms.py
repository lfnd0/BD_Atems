from django import forms

from .models import Local, Distribuidora

class DistribuidoraForm(forms.ModelForm):
    local = forms.ModelMultipleChoiceField(
        queryset=Local.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Distribuidora
        fields = ('nome', 'local', )