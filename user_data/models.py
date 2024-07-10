from django.db import models
from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100, choices=settings.USER_ROLES)
    registered = models.BooleanField(default=False)
    
class Data(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    business_unit = models.CharField(max_length=255)
    other_data = models.JSONField()
    valid_data = models.BooleanField(default=False)
    
class DataTransaction(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='data_transaction')
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'data_created_by')
    