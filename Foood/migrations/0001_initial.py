# Generated by Django 3.1.4 on 2021-01-05 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exfd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('FM', 'FeMale')], max_length=10)),
                ('rollno', models.CharField(max_length=10)),
                ('collegename', models.CharField(choices=[('AANM', 'AANM & VVRSR Polytechnic'), ('SVGP', 'S.V Govt polytechnic'), ('AANMR', 'AANM & VVRSR Polytechnic - RJYD')], max_length=7)),
                ('impf', models.ImageField(default='background1.jpg', upload_to='Profile/')),
                ('d', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
