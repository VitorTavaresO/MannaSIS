# Generated by Django 4.1.7 on 2023-02-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_alter_member_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo da Bolsa')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da Bolsa')),
                ('dateStart', models.DateField(verbose_name='Data de Início da Bolsa')),
                ('dateEnd', models.DateField(verbose_name='Data de Finalização da Bolsa')),
                ('description', models.CharField(max_length=2000, verbose_name='Descrição')),
                ('relatory', models.FileField(blank=True, upload_to='./static/uploads/relatory/scholarship', verbose_name='Relatório')),
            ],
        ),
    ]
