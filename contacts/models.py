from django.db import models
from datetime import datetime

# Create your models here.
class contacts(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    car_id =models.IntegerField()
    customer_need =models.CharField(max_length=100)
    car_title =models.CharField(max_length=100)
    city =models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    message =models.TextField(blank=True)
    user_id =models.CharField(max_length=100)
    created_date =models.DateTimeField(blank=True, default=datetime.now)
    
    def __self__(self):
        return self.email

    

    

