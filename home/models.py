from django.db import models


class Task(models.Model):
    Prioridad = (('B', 'Baja'),
                ('M', 'Media'),
                ('A', 'Alta'))

    Nombre_de_la_tarea = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    completed = models.BooleanField(default=False)
    prioridad = models.CharField(max_length=1, choices=Prioridad, default='B')

    def __str__(self):
        return self.Nombre_de_la_tarea
