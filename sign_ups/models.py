from django.db import models
from general.models import *
from applications.models import *
from opportunities.models import *
from tm.models import *
# Create your models here.


class EP(models.Model):
    member = models.ForeignKey('general.Member', related_name='ep_member', on_delete=models.CASCADE
                               , null=True, blank=True)
    managers = models.ManyToManyField('general.Member', related_name='ep_managers')
    date_of_sign_up = models.DateTimeField(null = True, blank = True)
    applications_count = models.IntegerField(default=0, null=True, )
    opportunities_applied_to = models.ManyToManyField('opportunities.Opportunity', related_name='ep_opportunities')
    selected_program = models.ForeignKey('applications.Product', related_name='product', on_delete=models.CASCADE
                                         , null=True, blank=True)
    contacted_at = models.DateTimeField(null = True, blank = True)
    contacted_by = models.ForeignKey('general.Member', related_name='ep_contacted_by', on_delete=models.CASCADE
                                     , null=True, blank=True)
    status = models.ForeignKey('applications.Status', related_name='ep_status', on_delete=models.CASCADE, null=True,
                               blank=True)
    applications = models.ForeignKey('applications.Application', related_name='ep_applications',
                                     on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "EP"


