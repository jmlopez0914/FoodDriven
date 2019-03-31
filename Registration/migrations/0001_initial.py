# Generated by Django 2.0.3 on 2019-03-23 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('home_Address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=20)),
                ('pickup_date', models.DateTimeField(default=datetime.datetime(2019, 3, 25, 6, 48, 35, 846573))),
            ],
        ),
    ]