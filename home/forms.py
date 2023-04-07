from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nombre_de_la_tarea', 'due_date']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nombre_de_la_tarea', 'due_date', 'prioridad', 'completed']
