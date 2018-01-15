# Generated by Django 2.0.1 on 2018-01-15 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gpio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stan', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Urzadzenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_ser', models.CharField(max_length=100)),
                ('Nazwa', models.CharField(max_length=250)),
                ('Seria', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='gpio',
            name='urzadzenie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esp.Urzadzenie'),
        ),
    ]
