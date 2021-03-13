from django.db import models

from opportunities.models import *
from sign_ups.models import *
from tm.models import *
from general.models import *
from ams.models import *

# Create your models here.

class OperationalFlow(models.Model):
    sign_up = models.BooleanField(default=False)    
    applied = models.BooleanField(default=False)    
    accepted_by_host = models.BooleanField(default=False)    
    accepted = models.BooleanField(default=False)    
    realized = models.BooleanField(default=False)    
    finished = models.BooleanField(default=False)    
    complete = models.BooleanField(default=False)    
    re_approved = models.BooleanField(default=False)    
    approved = models.BooleanField(default=False)    
    contacted = models.BooleanField(default=False)    
    realization_broken = models.BooleanField(default=False)    
    approval_broken = models.BooleanField(default=False)    
    rejected = models.BooleanField(default=False)    
    withdrawn = models.BooleanField(default=False)    
    pending_enabler_acceptance = models.BooleanField(default=False)    
    out_of_process = models.BooleanField(default=False)    


class Program(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SDG(models.Model):
    name = models.CharField(max_length=255)
    target = models.DecimalField(max_digits=255, decimal_places = 2)


class SubProduct(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Duration(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Application(models.Model):
    host_lc = models.ForeignKey('general.Entity', related_name='applications.host_lc+', on_delete=models.CASCADE)
    host_mc = models.ForeignKey('general.Entity', related_name='applications.host_mc+', on_delete=models.CASCADE)
    home_lc = models.ForeignKey('general.Entity', related_name='applications.home_lc+', on_delete=models.CASCADE)
    home_mc = models.ForeignKey('general.Entity', related_name='applications.home_mc+', on_delete=models.CASCADE)
    ep = models.ForeignKey('sign_ups.EP', related_name='applications.eb+', on_delete=models.CASCADE)
    application_manager = models.ForeignKey('general.Member', related_name='applications.app_manager+', on_delete=models.CASCADE)
    is_ir = models.BooleanField()
    status = models.ForeignKey(OperationalFlow, related_name='applications.status+', on_delete=models.CASCADE)
    process_time_SU_APL = models.DurationField()
    process_time_APL_ACC = models.DurationField()
    process_time_APL_APD = models.DurationField()
    process_time_SU_contacted = models.DurationField()
    process_time_APL_contacted = models.DurationField()
    tags = models.ForeignKey('general.Tag', related_name='applications.tag+', on_delete=models.CASCADE)
    notes = models.TextField()
    applied_at = models.DateField()
    accepted_at = models.DateField()
    approved_at = models.DateField()
    realized_at = models.DateField()
    accepted_by = models.ForeignKey('general.Member', related_name='applications.accepted_by+', on_delete=models.CASCADE)
    approved_by = models.ForeignKey('general.Member', related_name='applications.approved_by+', on_delete=models.CASCADE)
    realized_by = models.ForeignKey('general.Member', related_name='applications.realized_by+', on_delete=models.CASCADE)
    contacted_by = models.ForeignKey('general.Member', related_name='applications.contacted_by+', on_delete=models.CASCADE)
    re_approved_by = models.ForeignKey('general.Member', related_name='applications.reapproved_by+', on_delete=models.CASCADE)
    cv_filtered_by = models.ForeignKey('general.Member', related_name='applications.cv_filterd_by+', on_delete=models.CASCADE)
    program = models.ForeignKey(Program, related_name='applications.program+', on_delete=models.CASCADE)
    sdg = models.ForeignKey(SDG, related_name='applications.sdg+', on_delete=models.CASCADE)
    sub_product = models.ForeignKey(SubProduct, related_name='applications.sub_product+', on_delete=models.CASCADE)
    duration = models.ForeignKey(Duration, related_name='applications.duration+', on_delete=models.CASCADE)
    tn_fees = models.ForeignKey('opportunities.Opportunity', related_name='applications.tn_fees+', on_delete=models.CASCADE)
    contract_price = models.IntegerField()
