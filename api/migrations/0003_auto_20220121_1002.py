# Generated by Django 3.2.9 on 2022-01-21 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220121_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='clicked_times',
        ),
        migrations.RemoveField(
            model_name='site',
            name='long_url',
        ),
        migrations.RemoveField(
            model_name='site',
            name='short_url',
        ),
        migrations.AddField(
            model_name='site',
            name='clicked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='site',
            name='long',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='short',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
