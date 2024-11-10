from django.db import models

class Sales(models.Model):
    month = models.CharField(max_length=20)
    sales = models.IntegerField()

    # models.py
from django.db import models

class SalesData(models.Model):
    month = models.CharField(max_length=20,primary_key=True)
    sales = models.IntegerField()

    class Meta:
        db_table = 'sales_data2'  



class Inventory(models.Model):
    pass


class Expenses(models.Model):
    pass
