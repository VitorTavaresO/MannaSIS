# Generated by Django 4.1.7 on 2023-02-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_rename_quantidadealunos_hub_amountstudents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.IntegerField(max_length=50, verbose_name='Nome Completo'),
        ),
    ]
