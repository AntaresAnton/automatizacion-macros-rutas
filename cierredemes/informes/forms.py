# informes/forms.py

from .models import Proceso, Informe
from django import forms
from .models import Proceso
from django import forms
from .models import Informe

# class ProcesoForm(forms.ModelForm):
#     class Meta:
#         model = Proceso
#         fields = ['nombre', 'descripcion', 'orden', 'activo']




class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['nombre', 'descripcion', 'orden', 'activo']



# class InformeForm(forms.ModelForm):
#     class Meta:
#         model = Informe
#         fields = ['nombre', 'proceso', 'workflow', 'macro_path', 'source_path', 'destination_path', 'email_recipients', 'email_message', 'secuencial']



class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['proceso', 'nombre', 'workflow', 'macro', 'source_path', 'destination_path', 'email_recipients', 'email_message', 'is_sequential']
