# Generated by Django 3.1.7 on 2021-03-24 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_code', models.CharField(max_length=20, unique=True)),
                ('start_date', models.DateField()),
                ('status', models.CharField(choices=[('yet to begin', 'yet to begin'), ('in progress', 'in progress'), ('completed', 'completed')], max_length=20)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crmautomation.course')),
            ],
        ),
    ]
