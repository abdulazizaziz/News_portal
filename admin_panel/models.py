from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    role = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Users'
        ordering = ['id']