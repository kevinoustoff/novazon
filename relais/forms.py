from django import forms
from .models import PointRelais

class PointRelaisForm(forms.ModelForm):
    gmanager_signature = forms.BooleanField(required=True)
    

    class Meta:
        model = PointRelais
        fields = ['first_name', 'last_name','quartier','numero_telephone', 'latitude', 'longitude', 'relay_name', 'gmanager_signature']

    def __init__(self, *args, **kwargs):
        super(PointRelaisForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['relay_name'].required = True
        self.fields['numero_telephone'].required = True
        self.fields['quartier'].required = True

    def clean_gmanager_signature(self):
        gmanager_signature = self.cleaned_data['gmanager_signature']
        if not gmanager_signature:
            raise forms.ValidationError("La signature du gérant est requise.")
            return False
        return True
