# Generated by Django 2.1.4 on 2018-12-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('app_launched', models.IntegerField(blank=True, null=True)),
                ('most_active_day_last_7_days', models.CharField(max_length=15)),
                ('number_of_days_active_last_7_days', models.IntegerField(blank=True, null=True)),
                ('most_launched_app_last_7_days', models.CharField(max_length=30)),
            ],
        ),
    ]
