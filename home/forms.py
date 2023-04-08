from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nombre_de_la_tarea', 'fecha_de_vencimiento']

    def clean(self):
        cleaned_data = super().clean()
        nombre_tarea = cleaned_data.get('Nombre_de_la_tarea')
        if not nombre_tarea:
            raise ValidationError('El nombre de la tarea es un campo requerido.')
    

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nombre_de_la_tarea', 'fecha_de_vencimiento', 'prioridad', 'completado']
