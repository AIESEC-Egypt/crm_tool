from django.db import models
from general.models import *


class Slot(models.Model):
    slot_id = models.IntegerField(null = True, blank = True, default = 0)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)
    application_close = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.slot_id


class Opportunity(models.Model):

    op_id = models.IntegerField(null=True, blank=True, default=0)
    title = models.CharField(max_length = 200, null = True, blank=True)
    applicants_count = models.IntegerField(null = True, blank=True)
    enabler = models.CharField(max_length = 200, null = True, blank=True)
    lc = models.CharField(max_length = 100, null = True, blank=True)
    mc = models.CharField(max_length = 100, null = True, blank=True)
    tn_fees = models.IntegerField(null = True, default = 0, blank=True)
    sdg = models.CharField(max_length = 200, null = True, blank=True)
    sub_product = models.CharField(max_length = 200, null = True, blank=True)
    slot = models.ManyToManyField(Slot, null=True, blank=True)
    op_managers = models.ManyToManyField('general.Member', null=True, blank=True)

    def __str__(self):
        return self.title
