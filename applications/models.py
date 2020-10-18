from django.db import models
from general import models as general_models
from opportunities import models as opportunities_models
from sign_ups import models as sign_ups_models

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
    target = models.DecimalField()


class SubProduct(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Duration(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Application(models.Model):
    host_lc = models.ForeignKey('general_models.Entity', related_name='applications', on_delete=models.CASCADE)
    host_mc = models.ForeignKey('general_models.Entity', related_name='applications', on_delete=models.CASCADE)
    home_lc = models.ForeignKey('general_models.Entity', related_name='applications', on_delete=models.CASCADE)
    home_mc = models.ForeignKey('general_models.Entity', related_name='applications', on_delete=models.CASCADE)
    ep = models.ForeignKey('sign_ups_models.EP', related_name='applications', on_delete=models.CASCADE)
    application_manager = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    is_ir = models.BooleanField()
    status = models.ForeignKey(OperationalFlow, related_name='applications', on_delete=models.CASCADE)
    process_time_SU_APL = models.DurationField()
    process_time_APL_ACC = models.DurationField()
    process_time_APL_APD = models.DurationField()
    process_time_SU_contacted = models.DurationField()
    process_time_APL_contacted = models.DurationField()
    tags = models.ForeignKey('general_models.Tag', related_name='applications', on_delete=models.CASCADE)
    notes = models.TextField()
    applied_at = models.DateField()
    accepted_at = models.DateField()
    approved_at = models.DateField()
    realized_at = models.DateField()
    accepted_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    approved_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    realized_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    contacted_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    re_approved_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    cv_filtered_by = models.ForeignKey('general_models.Member', related_name='applications', on_delete=models.CASCADE)
    program = models.ForeignKey(Program, related_name='applications', on_delete=models.CASCADE)
    sdg = models.ForeignKey(SDG, related_name='applications', on_delete=models.CASCADE)
    sub_product = models.ForeignKey(SubProduct, related_name='applications', on_delete=models.CASCADE)
    duration = models.ForeignKey(Duration, related_name='applications', on_delete=models.CASCADE)
    tn_fees = models.ForeignKey('opportunities_models.Opportunity', related_name='applications', on_delete=models.CASCADE)
    contract_price = models.IntegerField()
