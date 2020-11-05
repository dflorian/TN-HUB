# Generated by Django 3.0.7 on 2020-06-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='body',
        ),
        migrations.AddField(
            model_name='paper',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AddField(
            model_name='paper',
            name='keywords',
            field=models.TextField(default='keywords'),
        ),
        migrations.AddField(
            model_name='paper',
            name='references',
            field=models.TextField(default='references'),
        ),
    ]