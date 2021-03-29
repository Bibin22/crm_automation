# Generated by Django 3.1.7 on 2021-03-29 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='course_name',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='course',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='admission_number',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='eid',
        ),
        migrations.DeleteModel(
            name='Admissions',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
