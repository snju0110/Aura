# Generated by Django 4.0.8 on 2023-04-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docdata',
            name='document_number',
            field=models.CharField(default='Not Entered', max_length=200),
        ),
    ]
