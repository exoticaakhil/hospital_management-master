# Generated by Django 4.2.3 on 2023-12-06 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_patient_patientid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patientid',
        ),
    ]
