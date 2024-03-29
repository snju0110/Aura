# Generated by Django 3.2.15 on 2023-09-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocManager', '0004_auto_20230904_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='doc_holder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Holder', models.CharField(default='NA', max_length=200)),
                ('full_name', models.CharField(default='NA', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='doc_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('cat1', models.CharField(default='NA', max_length=200)),
                ('cat2', models.CharField(default='NA', max_length=200)),
            ],
        ),
    ]
