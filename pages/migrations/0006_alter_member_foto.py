# Generated by Django 4.1.7 on 2023-02-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_member_planotrabalho_alter_member_termociencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='foto',
            field=models.ImageField(upload_to='./static/uploads/photos/', verbose_name='Foto'),
        ),
    ]
