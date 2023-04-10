# Generated by Django 4.1.7 on 2023-04-10 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_delete_awards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='award',
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('atype', models.CharField(max_length=100, verbose_name='Tipo de Prêmio')),
                ('organization', models.CharField(max_length=200, verbose_name='Premiador')),
                ('description', models.CharField(max_length=2000, verbose_name='Descrição')),
                ('pdf', models.FileField(upload_to='./static/uploads/award', verbose_name='Prêmio')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pages.member', verbose_name='Membro')),
            ],
        ),
    ]
