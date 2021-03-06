# Generated by Django 3.1.5 on 2021-01-08 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Foood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='South',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(choices=[('al', 'Vada'), ('ab', 'Wheat upma')], max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('workstatus', models.CharField(choices=[('yes', 'completed'), ('no', 'Not completed')], max_length=5)),
                ('m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
