# Generated by Django 3.1.7 on 2021-03-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crmautomation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='fees',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
