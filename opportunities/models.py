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
    lc = models.ForeignKey('general.Entity', related_name = 'opportunity_lc', on_delete = models.CASCADE,
                           null = True, blank = True)
    mc = models.ForeignKey('general.Entity', related_name = 'opportunity_mc', on_delete = models.CASCADE,
                           null = True, blank = True)
    sdg = models.CharField(max_length = 200, null = True, blank=True)
    sub_product = models.CharField(max_length = 200, null = True, blank=True)
    slot = models.ManyToManyField(Slot, null=True, blank=True, related_name = 'opportunity_slots')
    op_managers = models.ManyToManyField('general.Member', null=True, blank=True, related_name = 'opportunity_managers')
    op_choices = (
        ("1", 'Draft'),
        ("2", 'Under Review'),
        ("3", 'Live'),
        ("4", 'Unpublished'),
        ("5", 'Expired'),
    )

    op_status = models.CharField(max_length = 1, choices = op_choices, blank = True, null = True, default = 'Draft')

    def __str__(self):
        return self.title
