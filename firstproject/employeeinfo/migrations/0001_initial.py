# Generated by Django 4.1.2 on 2022-11-02 07:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('name', models.CharField(editable=False, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('department', models.CharField(choices=[('two', 'Pharma'), ('one', 'vet')], max_length=200)),
                ('launchdate', models.DateField(verbose_name=datetime.date)),
                ('quantity', models.CharField(max_length=200)),
                
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('name', models.CharField(editable=False, max_length=200, primary_key=True, serialize=False, unique=True)),
                ('manufacturer', models.CharField(choices=[('one', 'Sri_Ram_Healthcare_Pvt_Ltd'), ('two', 'Ultra_Drugs'), ('three', 'Prosperity')], max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('composition', models.CharField(max_length=200)),
                ('storage', models.CharField(max_length=200)),
                ('prod', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.products')),
            ],
        ),
    ]
