from django.db import models
# from general import models as general_models
# from applications import models as applications_models
from opportunities.models import *
from tm.models import *
from applications.models import *
from ams.models import *
# Create your models here.

class EP(models.Model):
    managers = models.ManyToManyField('general.Member')
    date_of_sign_up = models.DateTimeField()
    applications_count = models.IntegerField(default=0)
    # user = 
    selected_program = models.ForeignKey('applications.Program', related_name='EPs', on_delete=models.CASCADE)
    contacted_at = models.DateTimeField()
    contacted_by = models.ForeignKey('general.Member', related_name='applications', on_delete=models.CASCADE)


    