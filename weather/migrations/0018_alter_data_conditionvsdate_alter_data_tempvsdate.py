# Generated by Django 4.1 on 2022-11-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0017_alter_data_today_temp_alter_data_today_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ConditionVsDate',
            field=models.ImageField(default='weather/images/Bag.jfif', upload_to='weather/images'),
        ),
        migrations.AlterField(
            model_name='data',
            name='TempVsDate',
            field=models.ImageField(default='weather/images/Bag.jfif', upload_to='weather/images'),
        ),
    ]
