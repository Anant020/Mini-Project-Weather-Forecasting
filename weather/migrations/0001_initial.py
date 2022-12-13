# Generated by Django 4.1 on 2022-11-16 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Phone', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('Email', models.EmailField(max_length=254)),
                ('Issue', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('State', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('Today_Temp', models.FloatField()),
                ('Today_wind', models.FloatField()),
                ('Today_condition', models.CharField(max_length=40)),
                ('Today_sunrise', models.TimeField()),
                ('Today_sunset', models.TimeField()),
                ('TempVsDate', models.ImageField(default='', upload_to='weather/images')),
                ('ConditionVsDate', models.ImageField(default='', upload_to='weather/images')),
            ],
        ),
    ]
