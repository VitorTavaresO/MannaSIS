# Generated by Django 4.1.7 on 2023-05-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='auth',
            field=models.BooleanField(default=False),
        ),
    ]