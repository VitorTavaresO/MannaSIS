# Generated by Django 4.1.4 on 2023-01-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_member_face_member_insta_member_link_member_twt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='lattes',
            field=models.CharField(default=0, max_length=50, verbose_name='Lattes'),
            preserve_default=False,
        ),
    ]
