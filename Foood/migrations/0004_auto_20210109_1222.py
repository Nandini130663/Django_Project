# Generated by Django 3.1.5 on 2021-01-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foood', '0003_auto_20210109_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exfd',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('FM', 'FeMale'), ('Others', 'Others')], max_length=10),
        ),
    ]
