# Generated by Django 3.1.7 on 2021-03-31 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crm', '0005_auto_20210330_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissions',
            name='date',
            field=models.DateField(default=datetime.date(2021, 3, 31)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=datetime.date(2021, 3, 31)),
        ),
    ]
