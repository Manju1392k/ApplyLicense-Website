from django.db import models

# Create your models here.
class ApplyLicense(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=3)
    Father_Name = models.CharField(max_length=100)
    Scc_Number = models.CharField(max_length=11)
    Adhar_Number = models.CharField(max_length=12)

    def __str__(self):
        return self.Name
