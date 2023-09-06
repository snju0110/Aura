# Generated by Django 3.2.15 on 2023-09-04 10:17

import DocManager.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocManager', '0006_delete_docma'),
    ]

    operations = [
        migrations.CreateModel(
            name='docma',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('holder', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to=DocManager.models.upload_setup)),
                ('document_back', models.FileField(upload_to=DocManager.models.upload_setup_back)),
                ('desc', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('cat1', models.CharField(default='NA', max_length=200)),
                ('cat2', models.CharField(default='NA', max_length=200)),
                ('value', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('end_date', models.DateField()),
                ('time_stamp', models.DateTimeField()),
                ('remarks', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
            ],
        ),
    ]
