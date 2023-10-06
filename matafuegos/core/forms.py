from django import forms
import re

class AltaForms(forms.Form):
    nombre = forms.CharField(label="Nombre de Cliente", required=True)
    email = forms.CharField(label="Mail del Cliente", required=True)
    celular = forms.CharField(label="Celular del Cliente", required=True)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Validar que no contiene números
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError("El nombre no puede contener números.")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
       
        if '@' not in email:
            raise forms.ValidationError("El formato del correo electrónico no es válido.")
        return email

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')
        # Validar la estructura del celular (XX XXX XXX XXXX)
        if not re.match(r'^\d{2}\s\d{3}\s\d{3}\s\d{4}$', celular):
            raise forms.ValidationError("El formato del número de celular no es válido. Debe tener el formato XX XXX XXX XXXX.")
        return celular
