from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return f"{self.name} by {self.email}"
 
    