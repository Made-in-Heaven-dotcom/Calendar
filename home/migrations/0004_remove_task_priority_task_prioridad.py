# Generated by Django 4.2 on 2023-04-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
        migrations.AddField(
            model_name='task',
            name='prioridad',
            field=models.CharField(choices=[('B', 'Baja'), ('M', 'Media'), ('A', 'Alta')], default='B', max_length=1),
        ),
    ]
