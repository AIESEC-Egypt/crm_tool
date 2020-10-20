from django.db import models
from general import models as general_models
from applications import models as applications_models

# Create your models here.

class EP(models.Model):
    managers = models.ManyToManyField('general_models.Member') 
    date_of_sign_up = models.DateTimeField()
    applications_count = models.IntegerField(default=0)
    # user = 
    selected_program = models.ForeignKey('applications_models.Program', related_name='EPs', on_delete=models.CASCADE)
    contacted_at = models.DateTimeField()
    contacted_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)


    