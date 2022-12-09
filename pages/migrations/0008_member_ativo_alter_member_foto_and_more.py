# Generated by Django 4.1.4 on 2022-12-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_member_dtnasc'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ativo',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='foto',
            field=models.ImageField(upload_to='static/uploads/photos/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='member',
            name='termoCompromisso',
            field=models.FileField(upload_to='static/uploads/termos/', verbose_name='Termo de Compromisso'),
        ),
    ]