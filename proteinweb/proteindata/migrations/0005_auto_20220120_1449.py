# Generated by Django 3.0.3 on 2022-01-20 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proteindata', '0004_protein_protein_sequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='domain_ID',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='protein',
        ),
        migrations.DeleteModel(
            name='Organism',
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.DeleteModel(
            name='Pfam',
        ),
        migrations.DeleteModel(
            name='Protein',
        ),
    ]
