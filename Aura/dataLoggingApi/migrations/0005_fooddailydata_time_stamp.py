# Generated by Django 4.0.8 on 2023-06-10 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dataLoggingApi', '0004_fooddailydata'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddailydata',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
