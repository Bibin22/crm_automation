# Generated by Django 3.1.7 on 2021-03-30 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crm', '0003_auto_20210330_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2021, 3, 30)),
        ),
    ]
