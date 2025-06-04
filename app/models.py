from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    sport = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=30)
    class Meta:
        db_table = 'student'