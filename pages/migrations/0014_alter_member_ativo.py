# Generated by Django 4.1.4 on 2022-12-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_member_dtnasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='ativo',
            field=models.BooleanField(default=True, null=True),
        ),
    ]