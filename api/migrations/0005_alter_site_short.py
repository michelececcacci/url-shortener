# Generated by Django 4.0.1 on 2022-02-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220123_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='short',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]