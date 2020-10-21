from django.db import models
from general.models import *
# Create your models here.


class Pipeline(models.Model):
    pipeline_types = (
            ("LCP", 'Local Committee President'),
            ("LCVP", 'Local Committee Vice President'),
            ("TL", 'Team Leader'),
            ("COO", 'Coordinator'),
            ("NA", 'Not Interested'),
    )

    pipeline_type = models.CharField(max_length = 4, choices = pipeline_types, default = 'Not Interested')

    def __str__(self):
        return self.pipeline_type



def safe_div(x, y):
    if y == 0:
        return 0
    return x / y


class PlannedVsAchieved(models.Model):
    planned = models.ManyToManyField('general.OperationalGoal', null=True, blank=True, related_name = 'PvsA')
    achieved = models.IntegerField(null=True, blank=True, default=0)
    percentage = models.IntegerField(null=True, blank=True, default=0)

    def save(self, *args, **kwargs):

        self.percentage = round((safe_div(self.achieved, self.planned) * 100), 2)

        super(PlannedVsAchieved, self).save(*args, **kwargs)

    def __str__(self):
        return "{}%".format(self.percentage)


class TeamCreation(models.Model):
    transition = models.IntegerField(null = True, blank = True, default = 0)
    competence = models.IntegerField(null = True, blank = True, default = 0)
    team_rules = models.IntegerField(null = True, blank = True, default = 0)


class TeamPlan(models.Model):
    team_purpose = models.IntegerField(null = True, blank = True, default = 0)
    goals = models.IntegerField(null = True, blank = True, default = 0)
    strategies = models.IntegerField(null = True, blank = True, default = 0)
    timeline = models.IntegerField(null = True, blank = True, default = 0)
    jds = models.IntegerField(null = True, blank = True, default = 0)
    budget = models.IntegerField(null = True, blank = True, default = 0)
    team_development = models.IntegerField(null = True, blank = True, default = 0)


class IndividualPlan(models.Model):
    initial_lda = models.IntegerField(null = True, blank = True, default = 0)
    pdp = models.IntegerField(null = True, blank = True, default = 0)


class Building(models.Model):
    team_creation = models.ForeignKey(TeamCreation, null = True, blank = True,
                                      on_delete = models.CASCADE, related_name = 'building.creation')
    team_plan = models.ForeignKey(TeamPlan, null = True, blank = True,
                                  on_delete = models.CASCADE, related_name = 'building.team_plan')
    individual_plan = models.ForeignKey(IndividualPlan, null = True, blank = True,
                                        on_delete = models.CASCADE, related_name = 'building.individual_plan')


class ResultsEvaluation(models.Model):
    practical_learning = models.IntegerField(null = True, blank = True, default = 0)
    working_times = models.IntegerField(null = True, blank = True, default = 0)
    incentives = models.IntegerField(null = True, blank = True, default = 0)


class PerformanceTracking(models.Model):
    accountability_system = models.IntegerField(null = True, blank = True, default = 0)
    individual_tracking = models.IntegerField(null = True, blank = True, default = 0)
    team_reviews = models.IntegerField(null = True, blank = True, default = 0)


class SupportSystem(models.Model):
    lead_spaces = models.IntegerField(null = True, blank = True, default = 0)
    team_meetings = models.IntegerField(null = True, blank = True, default = 0)
    o2o = models.IntegerField(null = True, blank = True, default = 0)
    team_days = models.IntegerField(null = True, blank = True, default = 0)
    feedback = models.IntegerField(null = True, blank = True, default = 0)


class Performing(models.Model):
    results_elevation = models.ForeignKey(ResultsEvaluation, null = True, blank = True,
                                          on_delete = models.CASCADE, related_name = 'performing.result')
    performance_tracking = models.ForeignKey(PerformanceTracking, null = True, blank = True,
                                             on_delete = models.CASCADE, related_name = 'performing.tracking')
    support_system = models.ForeignKey(SupportSystem, null = True, blank = True,
                                       on_delete = models.CASCADE, related_name = 'performing.support_system')


class TeamDebrief(models.Model):
    reporting = models.IntegerField(null = True, blank = True, default = 0)
    team_development_review = models.IntegerField(null = True, blank = True, default = 0)
    feedback = models.IntegerField(null = True, blank = True, default = 0)


class Transition(models.Model):
    knowledge_and_skills = models.IntegerField(null = True, blank = True, default = 0)
    documents_and_tools = models.IntegerField(null = True, blank = True, default = 0)
    suggestions_of_way_forward = models.IntegerField(null = True, blank = True, default = 0)


class IndividualTransition(models.Model):
    final_lda = models.IntegerField(null = True, blank = True, default = 0)
    final_pdp = models.IntegerField(null = True, blank = True, default = 0)


class Closing(models.Model):
    team_debrief = models.ForeignKey(TeamDebrief, null = True, blank = True,
                                     on_delete = models.CASCADE, related_name = 'closing.debrief')
    transition = models.ForeignKey(Transition, null = True, blank = True,
                                   on_delete = models.CASCADE, related_name = 'closing.transition')
    individual_transition = models.ForeignKey(IndividualTransition, null = True, blank = True,
                                              on_delete = models.CASCADE, related_name = 'closing.ind_transition')


class TeamStandards(models.Model):
    building = models.ForeignKey(Building, null = True, blank = True,
                                 on_delete = models.CASCADE, related_name = 'building')
    performing = models.ForeignKey(Performing, null = True, blank = True,
                                   on_delete = models.CASCADE, related_name = 'performing')
    closing = models.ForeignKey(Closing, null = True, blank = True,
                                on_delete = models.CASCADE, related_name = 'closing')

    class Meta:
        verbose_name = "Team Standards"
        verbose_name_plural = "Team Standards"


class Nps(models.Model):
    nps = models.FloatField(null=True, blank=True, default=0)
    nps_explaination = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.nps)

    class Meta:
        verbose_name = "NPS"
        verbose_name_plural = "NPS"


class Nes(models.Model):
    member_name = models.ForeignKey('general.Member', null=True, blank=True,
                                    on_delete = models.CASCADE, related_name = 'nes.member_name')
    lc = models.ForeignKey('general.Entity', null=True, blank=True,
                           on_delete = models.CASCADE, related_name = 'nes.lc')
    role = models.ForeignKey('general.Role', null=True, blank=True,
                             on_delete = models.CASCADE, related_name = 'nes.role')
    department = models.ForeignKey('general.Department', null=True,
                                   blank=True, on_delete = models.CASCADE, related_name = 'nes.department')
    tl_satisfaction = models.IntegerField(null=True, blank=True, default=0)
    percentage_of_goal_achievement = models.ForeignKey(PlannedVsAchieved, null=True, blank=True,
                                                       on_delete = models.CASCADE, related_name = 'nes.goal_ach')
    engagement = models.IntegerField(null=True, blank=True, default=0)
    pipeline = models.ManyToManyField(Pipeline, null=True, blank=True, default=0, related_name = 'nes.pipeline')
    team_standards = models.ForeignKey(TeamStandards, null = True,
                                       blank = True, on_delete = models.CASCADE, related_name = 'nes.ts')
    nps = models.ForeignKey(Nps, null = True, blank = True,
                            on_delete = models.CASCADE, related_name = 'nes.nps')
    class Meta:
        verbose_name = "NES"
        verbose_name_plural = "NES"
