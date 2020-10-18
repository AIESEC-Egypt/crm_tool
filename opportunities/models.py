from django.db import models
from general.models import Member

# Create your models here.


class Slot(models.Model):
    slot_id = models.IntegerField(null = True, blank = True, default = 0)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)
    application_close = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.slot_id


class Opportunity(models.Model):

    op_id = models.IntegerField(null=True, blank=True, default=0)
    title = models.CharField(max_length = 200, null = True)
    applicants_count = models.IntegerField(null = True)
    enabler = models.CharField(max_length = 200, null = True)
    lc = models.models.CharField(max_length = 100, null = True)
    mc = models.models.CharField(max_length = 100, null = True)
    tn_fees = models.IntegerField(null = True, default = 0)
    sdg = models.CharField(max_length = 200, null = True)
    sub_product = models.CharField(max_length = 200, null = True)
    slot = models.ManyToManyField(Slot, null=True, blank=True)
    op_manager = models.ManyToManyField(Member, null=True, blank=True)

    def __str__(self):
        return self.title
