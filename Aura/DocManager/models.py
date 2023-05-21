from django.db import models

# Create your models here.


class DocData(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    user = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    document_name = models.CharField(max_length=200)
    document_type = models.CharField(max_length=200)
    document_remarks = models.CharField(max_length=200)
    document_number = models.CharField(max_length=200 , default='Not Entered')
    document_path = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)

    def __str__(self):
        return self.document_name