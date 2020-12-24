from django.db import models
from django.db import connections

class Student(models.Model):
    Student_name= models.CharField(max_length=50)
    USN= models.CharField(max_length=10)
    Email_id= models.CharField(max_length=20)
    Phone_number= models.IntegerField()
    Event_name= models.CharField(max_length=50)
    class Meta:
        db_table="student"