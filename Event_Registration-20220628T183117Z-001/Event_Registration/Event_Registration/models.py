from django.db import models

class CustModel(models.Model):
    c_id=models.BigIntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    c_email=models.CharField(max_length=40)
    c_Bdate=models.DateField()
    c_phno=models.BigIntegerField()
    password=models.CharField(max_length=64)
    age=models.IntegerField()
    class Meta:
        db_table = "customer"  


class EventModel(models.Model):
    event_id=models.BigIntegerField(primary_key=True)
    e_type_id=models.BigIntegerField()
    e_name=models.CharField(max_length=100)
    e_date=models.DateField()
    e_size=models.IntegerField()
    address_line_1=models.CharField(max_length=50)
    address_line_2=models.CharField(max_length=50)
    pincode=models.IntegerField()
    e_manager=models.IntegerField()
    class Meta:
        db_table = "event"  