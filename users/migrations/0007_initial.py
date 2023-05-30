# Generated by Django 4.1.7 on 2023-05-29 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_remove_status_user_delete_statustype_delete_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(choices=[('DIRETORIA', 'Diretoria'), ('LIDER DE HUB', 'Lider de Hub'), ('MEMBRO', 'Membro')], default='MEMBRO', max_length=50, verbose_name='Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]