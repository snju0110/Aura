import os.path

from django.db import models


# Create your models here.


class DocData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    document_name = models.CharField(max_length=200)
    document_type = models.CharField(max_length=200)
    document_remarks = models.CharField(max_length=200)
    document_number = models.CharField(max_length=200, default='Not Entered')
    document_path = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)

    def __str__(self):
        return self.document_name


def upload_setup(instances, filename):
    ext = os.path.splitext(filename)[1]
    type = instances.type
    holder = instances.holder
    number = instances.number

    path = 'static/Docma/' + type + '/' + holder + '_' + number + '_front' + ext
    return path


def upload_setup_back(instances, filename):
    ext = os.path.splitext(filename)[1]
    type = instances.type
    holder = instances.holder
    number = instances.number

    path ='static/Docma/' + type + '/' + holder + '_' + number + '_back' + ext
    return path


class docma(models.Model):
    id = models.IntegerField(primary_key=True)
    holder = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    document = models.FileField(upload_to=upload_setup)
    document_back = models.FileField(upload_to=upload_setup_back , blank=True,default='default.png')
    desc = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    cat1 = models.CharField(max_length=200, default='NA')
    cat2 = models.CharField(max_length=200, default='NA')
    value = models.IntegerField(default=0)
    date = models.DateField()
    end_date = models.DateField()
    time_stamp = models.DateTimeField()
    remarks = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class doc_type(models.Model):
    type = models.CharField(max_length=200)
    cat1 = models.CharField(max_length=200, default='NA')
    cat2 = models.CharField(max_length=200, default='NA')

    def __str__(self):
        return self.type


class doc_holder(models.Model):
    Holder = models.CharField(max_length=200, default='NA')
    full_name = models.CharField(max_length=200, default='NA')

    def __str__(self):
        return self.Holder
