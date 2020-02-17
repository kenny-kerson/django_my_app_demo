from django.db import models

class Customer(models.Model):
    cstno = models.CharField(max_length=16, primary_key=True, default=" ")
    cust_kor_nm = models.CharField(max_length=50)

    class Meta:
        db_table = "customer"