from django.db import models

# Create your models here.
class members(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Join_Date=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"