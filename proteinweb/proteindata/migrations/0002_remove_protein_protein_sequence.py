# Generated by Django 3.0.3 on 2022-01-20 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proteindata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protein',
            name='protein_sequence',
        ),
    ]
