from django.db import models

class Account(models.Model):
    account_no = models.CharField(max_length=255)
    account_status = models.CharField(max_length=255)
    user_id = models.CharField(max_length=32)

class Customer(models.Model):
    cstno = models.CharField(max_length=16)
    cust_kor_nm = models.CharField(max_length=50)