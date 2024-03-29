from django.db import models
from django.contrib.auth.models import User
from opportunities.models import *
from tm.models import *
from sign_ups.models import *
# Create your models here.


class Entity(models.Model):
    name = models.CharField(max_length=250)
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name = 'entity_parent')

    def __str__(self):
        return self.name


class Address(models.Model):
    building_number = models.CharField(max_length=250, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    governerate = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "Building {}, Street {}, City {}, District {}, Governerate {}"\
            .format(self.building_number, self.street, self.district, self.city, self.governerate)


class Department(models.Model):
    name = models.CharField(max_length=250)
    department_id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Role(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name = 'role_department')
    level = (
        ("1", 'Member'),
        ("2", 'Coordinator'),
        ("3", 'LCVP'),
        ("4", 'LCP'),
        ("5", 'EDT'),
        ("6", 'EDT TL'),
        ("7", 'RST'),
        ("8", 'GST'),
        ("9", 'ECB Chair'),
        ("10", 'ECB Director'),
        ("11", 'ECB Member'),
        ("12", 'EFB Chair'),
        ("13", 'EFB Director'),
        ("14", 'EFB Member'),
        ("15", 'MCVP'),
        ("16", 'MCP'),
        ("17", 'Alumnus'),
        ("xx", 'Other'),

    )
    hierarchy = models.CharField(max_length = 2, choices = level, default = 'Other')
    lc = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True, related_name = 'role_lc')
    is_leading_a_team = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    # productivity
    # retention
    # nps
    # pipeline
    # team_standards

    def __str__(self):
        return self.hierarchy


class Skill(models.Model):
    skill = models.CharField(max_length=100, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    expa_id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.skill


class Language(models.Model):
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=100)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Background(models.Model):
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=100)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.tag


class TouchPoints(models.Model):
    meeting_host_entity = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE,
                                            related_name = 'meeting_entity')
    meeting_id = models.IntegerField(null=True, blank=True, default=0)
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    meeting_name = models.CharField(max_length = 250, null = True, blank = True, default = 0)
    meeting_types = (
        ("1", 'National Conference'),
        ("2", 'Local Conference'),
        ("3", 'LCM'),
        ("4", 'MCM'),
        ("5", 'Comission Meeting'),
        ("6", 'Functional Visit'),
        ("7", 'OD Visit'),
        ("8", 'o2o'),
        ("9", 'Commission Meeting'),
        ("10", 'Functional Meeting'),
        ("11", 'TLs Meeting'),
        ("12", 'EB Meeting'),
        ("13", 'Management Team Meeting'),
        ("14", 'OD Meeting'),
        ("15", 'OPS Meeting'),
        ("16", 'Brand Meeting'),
        ("17", 'Finance Meeting'),
        ("18", 'EDTs Meeting'),
        ("19", 'IR Meeting'),
        ("20", 'LC Outing'),
        ("21", 'Team days'),
        ("XX", 'Other')
    )

    meeting_type = models.CharField(max_length = 2, choices = meeting_types, default = 'Other')
    audience = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name = 'meeting_audience')


class OperationalGoal(models.Model):
    goal_type = (
        ("SU", 'Sign UPs'),
        ("APL", 'Applied'),
        ("ACC", 'Accepted'),
        ("APD", 'Approved'),
        ("RE", 'Realized'),
        ("FI", 'Finished'),
        ("CO", 'Complete'),
        ("XX", "Choose a type")
    )
    goal = models.CharField(max_length = 3, choices = goal_type, default = 'XX')
    number = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return "{} {}".format(self.number, self.goal)


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'member')
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    atom_id = models.IntegerField(null=True, blank=True, default=0)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    lc = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True, related_name = 'member_lc')
    gender = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    whatsapp = models.CharField(max_length=250, null=True, blank=True)
    primary_email = models.CharField(max_length=250, null=True, blank=True)
    secondary_email = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True,
                                related_name = 'member_address')
    is_ixp = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,
                                   blank=True, related_name = 'member_department')
    role = models.ManyToManyField(Role, null=True, blank=True, related_name = 'member_roles')
    managed_ops = models.ManyToManyField('opportunities.Opportunity', null=True,
                                         blank=True, related_name = 'member_managed_ops')
    managed_eps = models.ManyToManyField('sign_ups.EP', null=True, blank=True, related_name = 'member_managed_eps')
    # managed_enablers
    # managed_partners
    backgrounds = models.ManyToManyField(Background, null=True, blank=True, related_name = 'member_backgrounds')
    languages = models.ManyToManyField(Language, null=True, blank=True, related_name = 'member_languages')
    skills = models.ManyToManyField(Skill, null=True, blank=True, related_name = 'member_skills')
    is_rxp = models.BooleanField(default=False)
    operational_goals = models.ForeignKey(OperationalGoal, on_delete=models.CASCADE, null=True,
                                          blank=True, related_name = 'member_operational_goals')
    status_choices = (
        ("1", 'Active Member'),
        ("2", 'Member on IXP'),
        ("3", 'Resigned'),
        ("4", 'Dismissed'),
        ("5", 'Under Probation'),
        ("6", 'Alumnus')
    )
    member_status = models.CharField(max_length = 1, choices = status_choices, default = 'Active Member')
    leaving_choices = (
        ("1", 'Own Decision'),
        ("2", 'Low Performance'),
        ("3", 'Low engagement'),
        ("4", 'Unethical Behavior'),
        ("5", 'Rules Violation'),
        ("6", 'Other')
    )
    reason_of_leaving = models.CharField(max_length = 1, choices = leaving_choices, blank = True, null = True,
                                         default = 'Other')
    membership_cycles = models.IntegerField(null=True, blank=True, default=0)
    completed_at_least_one_membership_cycle = models.BooleanField(default=False)
    touch_points = models.ForeignKey(TouchPoints, on_delete=models.CASCADE,
                                     null=True, related_name = 'member_touch_points')
    number_of_touch_points_hosted = models.IntegerField(null=True, blank=True, default=0)
    number_of_touch_points_attended = models.IntegerField(null=True, blank=True, default=0)
    number_of_touch_points_required_to_attend = models.IntegerField(null=True, blank=True, default=0)
    managed_applications_count = models.IntegerField(null=True, blank=True, default=0)
    managed_opportunities_count = models.IntegerField(null=True, blank=True, default=0)
    managed_eps_count = models.IntegerField(null=True, blank=True, default=0)
    managed_enablers_count = models.IntegerField(null=True, blank=True, default=0)
    managed_partners_count = models.IntegerField(null=True, blank=True, default=0)
    joined_atom_at = models.DateTimeField(null=True, blank=True)
    joined_expa_at = models.DateTimeField(null=True, blank=True)
    left_expa_at = models.DateTimeField(null=True, blank=True)
    left_expa = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='user-images/', null=True, blank=True)
    team_standards = models.ManyToManyField('tm.TeamStandards', null=True, blank=True,
                                            related_name = 'member_ts')
    members_nps = models.ForeignKey('tm.Nps', null=True, on_delete = models.CASCADE, related_name = 'member_nps')
    retention = models.IntegerField(null=True, blank=True, default=0)
    productivity = models.IntegerField(null=True, blank=True, default=0)
    notes = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='user-cv/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    operational_status = models.ManyToManyField('sign_ups.EP', null=True, blank=True,
                                                related_name = 'member_operational_status')

    def save(self, *args, **kwargs):
        self.full_name = "{} {}".format(self.first_name, self.last_name)

        if self.membership_cycles == 0:
            self.completed_atleast_one_membership_cycle = False
        else:
            self.completed_atleast_one_membership_cycle = True
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


