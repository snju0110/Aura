from django.db import models


# Create your models here.

class demDatatable(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    amount = models.IntegerField()
    sentFrom = models.CharField(max_length=200)
    sentTo = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    primaryCat = models.CharField(max_length=200)
    groupCat = models.CharField(max_length=200)

    def __str__(self):
        return self.user


class demDailyData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    amount = models.IntegerField()
    sentFrom = models.CharField(max_length=200)
    sentTo = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    primaryCat = models.CharField(max_length=200)
    groupCat = models.CharField(max_length=200)
    trip = models.CharField(max_length=200 ,  null=True)

    # class Meta:
    #     unique_together = ("amount", "sentFrom")

    def __str__(self):
        return self.user


class foodDailyData(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    time_stamp = models.DateTimeField()
    meal_type = models.CharField(max_length=200)
    meal_qty = models.IntegerField()
    category = models.CharField(max_length=200)
    junk =  models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=19, decimal_places=10)
    longitude = models.DecimalField(max_digits=19, decimal_places=10)


    def __str__(self):
        return self.user