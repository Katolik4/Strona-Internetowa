# Generated by Django 2.0.1 on 2018-01-13 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nowa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_titile',
            new_name='album_title',
        ),
    ]