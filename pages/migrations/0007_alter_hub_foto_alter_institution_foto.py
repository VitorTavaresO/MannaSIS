# Generated by Django 4.1.7 on 2023-02-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_member_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='foto',
            field=models.ImageField(upload_to='./static/uploads/photos/hub', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='foto',
            field=models.ImageField(upload_to='./static/uploads/photos/institution', verbose_name='Foto'),
        ),
    ]
