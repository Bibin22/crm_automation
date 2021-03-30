# Generated by Django 3.1.7 on 2021-03-30 04:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_number', models.CharField(max_length=20, unique=True)),
                ('fees', models.IntegerField()),
                ('date', models.DateField(default=datetime.date(2021, 3, 30))),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_code', models.CharField(max_length=20, unique=True)),
                ('start_date', models.DateField()),
                ('fees', models.IntegerField()),
                ('status', models.CharField(choices=[('yet to begin', 'yet to begin'), ('in progress', 'in progress'), ('completed', 'completed')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20, unique=True)),
                ('course_duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_id', models.CharField(max_length=20, unique=True)),
                ('student_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('qualification', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=100)),
                ('followup_date', models.DateField()),
                ('status', models.CharField(choices=[('admited', 'admited'), ('not admited', 'not admited')], max_length=20)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.batch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.course')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('admission_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.admissions')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.enquiry')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.course'),
        ),
        migrations.AddField(
            model_name='admissions',
            name='batch_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.batch'),
        ),
        migrations.AddField(
            model_name='admissions',
            name='eid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crm.enquiry'),
        ),
    ]
