# Generated by Django 3.0.3 on 2022-01-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteindata', '0002_remove_protein_protein_sequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protein',
            name='organism',
        ),
        migrations.AlterField(
            model_name='protein',
            name='protein_ID',
            field=models.CharField(blank=True, db_index=True, max_length=256),
        ),
    ]
