from django.db import models

class Account(models.Model):
    account_no = models.CharField(max_length=255, primary_key=True, default=" ")
    account_status = models.CharField(max_length=255)
    user_id = models.CharField(max_length=32)