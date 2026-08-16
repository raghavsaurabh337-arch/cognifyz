from django.db import models

# Create your models here.
class recode(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name

class create(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField()
    password=models.CharField(max_length=100)   
    def __str__(self):
        return self.name