from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Count


class Name(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name


class Entity(models.Model):
    name = models.CharField(max_length=250)
    expa_id = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):

    phone_number = models.CharField(max_length=250, null=True, blank=True)
    whatsapp = models.CharField(max_length=250, null=True, blank=True)
    primary_email = models.CharField(max_length=250, null=True, blank=True)
    secondary_email = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.phone

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
    department_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Role:
    department = models.ManyToManyField(Department, on_delete=models.CASCADE)
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
    expa_id = models.IntegerField()
    def __str__(self):
        return self.name

class Language(models.Model):
    expa_id = models.IntegerField()
    name = models.CharField(max_length=100)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



class Background(models.Model):
    expa_id = models.IntegerField()
    name = models.CharField(max_length=100)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.tag



class TagCount(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    tag_count = models.IntegerField(null=True, default=0)

    def tags_sum(self,Tag):
        self.tag_count = Tag.objects.filter(tag=Tag.tag).count()

    def __str__(self):
        return self.tag_count, self.tag

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expa_id = models.IntegerField(null=True, blank=True)
    atom_id = models.IntegerField(null=True, blank=True)
    first_name = models.OneToOneField(Name.first_name, on_delete=models.CASCADE)
    last_name = models.OneToOneField(Name.last, on_delete=models.CASCADE)
    full_name = models.OneToOneField(Name.full_name, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    lc = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.OneToOneField(ContactInfo.phone_number, on_delete=models.CASCADE)
    whatsapp = models.OneToOneField(ContactInfo.whatsapp, on_delete=models.CASCADE)
    primary_email = models.OneToOneField(ContactInfo.primary_email, on_delete=models.CASCADE)
    secondary_email = models.OneToOneField(ContactInfo.secondary_email, on_delete=models.CASCADE)
    facebook = models.OneToOneField(ContactInfo.facebook, on_delete=models.CASCADE)
    instagram = models.OneToOneField(ContactInfo.instagram, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address, on_delete=models.CASCADE)
    is_ixp = models.BooleanField(default=False)
    department = models.ManyToManyField(Department, on_delete=models.CASCADE)
    # applications
    role = models.ManyToManyField(Role, on_delete=models.CASCADE)
    # managed_eps
    # managed_ops
    # managed_enablers
    # managed_partners
    backgrounds = models.ManyToManyField(Background)
    languages = models.ManyToManyField(Language)
    skills = models.ManyToManyField(Skill)
    is_rxp = models.BooleanField(default=False)
    # operational_goals
    # membership_status
    # pipeline
    # touch_points
    # managed_applcations_count
    # managed_opportunities_count
    # managed_eps_count
    # managed_enablers_count
    # managed_partners_count
    joined_atom_at = models.DateTimeField(null=True, blank=True)
    joined_expa_at = models.DateTimeField(null=True, blank=True)
    left_expa_at = models.DateTimeField(null=True, blank=True)
    left_expa = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='user-images/')
    # team_standards =
    # members_nps =
    # retention
    # productivity
    notes = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='user-cv/')
    # operational_status
    tags = models.ManyToManyField(TagCount)



