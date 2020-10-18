from django.db import models
from django.contrib.auth.models import User
from opportunities.models import *

# Create your models here.


class Entity(models.Model):
    name = models.CharField(max_length=250)
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

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
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lc = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    is_leading_a_team = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    # productivity
    # retention
    # nps
    # pipeline
    # team_standards


class Skill(models.Model):
    skill = models.CharField(max_length=100, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.name

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


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expa_id = models.IntegerField(null=True, blank=True, default=0)
    atom_id = models.IntegerField(null=True, blank=True, default=0)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    lc = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    whatsapp = models.CharField(max_length=250, null=True, blank=True)
    primary_email = models.CharField(max_length=250, null=True, blank=True)
    secondary_email = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    is_ixp = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    # applications
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    managed_ops = models.ManyToManyField('opportunities.Opportunity', null=True, blank=True)
    # managed_eps
    # managed_enablers
    # managed_partners
    backgrounds = models.ManyToManyField(Background, null=True, blank=True)
    languages = models.ManyToManyField(Language, null=True, blank=True)
    skills = models.ManyToManyField(Skill, null=True, blank=True)
    is_rxp = models.BooleanField(default=False)
    # operational_goals
    status_choices = (
        (1, 'Active Member'),
        (2, 'Member on IXP'),
        (3, 'Resigned'),
        (4, 'Dismissed'),
        (5, 'Under Probation'),
        (6, 'Alumnus')
    )
    member_status = models.CharField(max_length = 1, choices = status_choices, default = 'Active Member')
    reason_of_leaving = models.TextField(blank = True, null = True)

    membership_cycles = models.IntegerField(null=True, blank=True, default=0)
    completed_one_membership_cycle = models.BooleanField(default=False)

    # pipeline
    # touch_points
    managed_applcations_count = models.IntegerField(null=True, blank=True, default=0)
    managed_opportunities_count = models.IntegerField(null=True, blank=True, default=0)
    managed_eps_count = models.IntegerField(null=True, blank=True, default=0)
    managed_enablers_count = models.IntegerField(null=True, blank=True, default=0)
    managed_partners_count = models.IntegerField(null=True, blank=True, default=0)
    joined_atom_at = models.DateTimeField(null=True, blank=True)
    joined_expa_at = models.DateTimeField(null=True, blank=True)
    left_expa_at = models.DateTimeField(null=True, blank=True)
    left_expa = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='user-images/', null=True, blank=True)
    # team_standards =
    # members_nps =
    # retention
    # productivity
    notes = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='user-cv/', null=True, blank=True)
    # operational_status
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_name = "{} {}".format(self.first_name, self.last_name)
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
