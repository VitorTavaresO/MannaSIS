# Generated by Django 4.1.3 on 2022-11-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='static/uploads/')),
                ('nome', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('instituicao', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fone', models.CharField(max_length=50)),
                ('git', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('rg', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('formacao', models.CharField(max_length=50)),
                ('dtnasc', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('projeto', models.CharField(max_length=50)),
                ('premio', models.CharField(max_length=50)),
            ],
        ),
    ]