# Generated by Django 4.1.7 on 2023-02-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_member_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome Completo'),
        ),
    ]
