from django.db import models

class applicants(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    mobilenumber=models.CharField(max_length=30)

    def __str__(self):
        return self.email
