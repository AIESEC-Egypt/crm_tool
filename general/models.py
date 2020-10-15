from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Name(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    def __str__(self):
        return self.full_name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expa_id = models.IntegerField(null=True, blank=True)
    atom_id = models.IntegerField(null=True, blank=True)
    first_name = models.OneToOneField(Name.first_name, on_delete=models.CASCADE)
    last_name = models.OneToOneField(Name.last, on_delete=models.CASCADE)
    full_name = models.OneToOneField(Name.full_name, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    


