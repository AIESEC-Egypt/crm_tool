# from django.db import models
# from general.models import *
# # Create your models here.
#
#
# class TeamStandards(models.Model):
#
#     pass
#
# # class Engagement(models.Model):
# #     engagement_types = (
# #         ("1", 'LCM on'),
# #         ("2", 'Local Conference'),
# #         ("3", 'LCM'),
# #         ("4", 'MCM'),
# #         ("5", 'Comission Meeting'),
# #         ("6", 'Functional Visit'),
# #         ("7", 'OD Visit'),
# #         ("8", 'o2o'),
# #         ("9", 'Comission Meeting'),
# #         ("10", 'Functional Meeting'),
# #         ("11", 'TLs Meeting'),
# #         ("12", 'EB Meeting'),
# #         ("13", 'Management Team Meeting'),
# #     )
# #
# #     engagement_type = models.CharField(max_length = 2, choices = engagement_types, default = 'Other')
#
#
# class Nes(models.Model):
#     member_name = models.ManyToManyField('general.Member', null=True, blank=True, on_delete = models.CASCADE)
#     lc = models.ManyToManyField('general.Entity', null=True, blank=True, on_delete = models.CASCADE)
#     role = models.ManyToManyField('general.Role', null=True, blank=True, on_delete = models.CASCADE)
#     department = models.ManyToManyField('general.Department', null=True, blank=True, on_delete = models.CASCADE)
#     recommending_aiesec_to_a_friend = models.IntegerField(null=True, blank=True, default=0)
#     tl_satisfaction = models.IntegerField(null=True, blank=True, default=0)
#     percentage_of_goal_achievement = models.IntegerField(null=True, blank=True, default=0)
#     # engagement = models.ManyToManyField(null=True, blank=True, default=0)
#     pipeline = models.ForeignKey(null=True, blank=True, default=0)
#     rating_explaination = models.TextField(null=True, blank=True)
#     building = models.ForeignKey(null=True, blank=True, default=0)
#     performance = models.ForeignKey(null=True, blank=True, default=0)
#     closing = models.ForeignKey(null=True, blank=True, default=0)
