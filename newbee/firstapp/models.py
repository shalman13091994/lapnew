from django.db import models

class person(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.TextField()

    def __str__(self):
     return self.firstname+" "+" | "+ self.lastname
