from django.db import models

# Create your models here.
class Model(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    email=models.CharField(max_length=15)
    mobile=models.IntegerField()
    address=models.CharField(max_length=300)
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    class Meta:
        db_table='MyApp'
