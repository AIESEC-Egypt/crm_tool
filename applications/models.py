from django.db import models
from general.models import *
from general.models import *
from opportunities.models import *
from sign_ups.models import *

# Create your models here.


class Status(models.Model):
    app_choices = (
        ("1", 'Sign Up'),
        ("2", 'Applied'),
        ("3", 'Accepted By Host'),
        ("4", 'Accepted'),
        ("5", 'Approved'),
        ("6", 'Realized'),
        ("7", 'Finished'),
        ("8", 'Complete'),
        ("9", 'Re-Approved'),
        ("10", 'Contacted'),
        ("11", 'Realization Broken'),
        ("12", 'Approval Broken'),
        ("13", 'Rejected'),
        ("14", 'Withdrawn'),
        ("15", 'Pending Enabler Acceptance'),
        ("16", 'Out Of Process'),

    )

    app_status = models.CharField(max_length = 1, choices = app_choices, blank = True, null = True, default = 'Sign Up')


class Program(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True, default=0)
    id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class SDG(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default=0)
    target = models.DecimalField()
    id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class SubProduct(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Duration(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Application(models.Model):
    application_id = models.IntegerField(null=True, blank=True, default=0)
    host_lc = models.ForeignKey('general.Entity', related_name='application.host_lc', on_delete=models.CASCADE,
                                null=True, blank=True)
    host_mc = models.ForeignKey('general.Entity', related_name='application.host_mc', on_delete=models.CASCADE
                                , null=True, blank=True)
    home_lc = models.ForeignKey('general.Entity', related_name='application.home_lc', on_delete=models.CASCADE
                                , null=True, blank=True)
    home_mc = models.ForeignKey('general.Entity', related_name='application.home_mc', on_delete=models.CASCADE
                                , null=True, blank=True)
    ep = models.ForeignKey('sign_ups.EP', related_name='application.ep', on_delete=models.CASCADE
                           , null=True, blank=True)
    application_manager = models.ForeignKey('general.Member', related_name='applications',
                                            on_delete=models.CASCADE, null=True, blank=True)
    is_ir = models.BooleanField(null=True, default = False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='application.status',
                               null=True, blank=True)
    process_time_SU_APL = models.IntegerField(null=True, blank=True, default=0)
    process_time_APL_ACC = models.IntegerField(null=True, blank=True, default=0)
    process_time_APL_APD = models.IntegerField(null=True, blank=True, default=0)
    process_time_SU_contacted = models.IntegerField(null=True, blank=True, default=0)
    process_time_APL_contacted = models.IntegerField(null=True, blank=True, default=0)
    tags = models.ForeignKey('general.Tag', related_name='application.tags', on_delete=models.CASCADE
                             , null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    applied_at = models.DateTimeField(null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    realized_at = models.DateTimeField(null=True, blank=True)
    accepted_by = models.ForeignKey('general.Member', related_name='application.accepted_by', on_delete=models.CASCADE
                                    , null=True, blank=True)
    approved_by = models.ForeignKey('general.Member', related_name='application.approved_by', on_delete=models.CASCADE
                                    , null=True, blank=True)
    realized_by = models.ForeignKey('general.Member', related_name='application.realized_by', on_delete=models.CASCADE
                                    , null=True, blank=True)
    contacted_by = models.ForeignKey('general.Member', related_name='application.contacted_by', on_delete=models.CASCADE
                                     , null=True, blank=True)
    re_approved_by = models.ForeignKey('general.Member', related_name='application.re_approved_by',
                                       on_delete=models.CASCADE, null=True, blank=True)
    cv_filtered_by = models.ForeignKey('general.Member', related_name='application.cv_filtered_by',
                                       on_delete=models.CASCADE, null=True, blank=True)
    program = models.ForeignKey(Program, related_name='application.program',
                                on_delete=models.CASCADE, null=True, blank=True)
    sdg = models.ForeignKey(SDG, related_name='application.sdg', on_delete=models.CASCADE, null=True, blank=True)
    sub_product = models.ForeignKey(SubProduct, related_name='application.sub_product', on_delete=models.CASCADE,
                                    null=True, blank=True)
    duration = models.ForeignKey(Duration, related_name='application', on_delete=models.CASCADE
                                 , null=True, blank=True)
    tn_fees = models.ForeignKey('opportunities.Opportunity', related_name='application.tn_fees',
                                on_delete=models.CASCADE, null=True, blank=True)
    contract_price = models.IntegerField(null=True, blank=True, default = 2400)
