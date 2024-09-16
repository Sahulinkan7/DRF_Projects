from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
