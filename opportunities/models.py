from django.db import models
# Create your models here.

class Meeting_ID(models.Model):
    meeting_id=models.UUIDField(editable=False)    
class Atom_ID(models.Model):
    atom_id=models.UUIDField(editable=False)   
class Expa_ID(models.Model):
    expa_id=models.UUIDField(editable=False)   
class Application_ID(models.Model):
    application_id=models.UUIDField(editable=False)     
class Enabler(models.Model):
    name=models.CharField(max_length=100)

class Entity(models.Model):
    application_id = models.ForeignKey(Application_ID,on_delete=models.CASCADE)
class Opportunity(models.Model):
    op_id=models.UUIDField(primary_key=True)
    title= models.CharField(max_length=100, null=False)
    applicants_count=models.IntegerField(null=False)
    application_close_date=models.DateField(null=False)
    slot_applied_to=models.DateField(null=False)
    openings=models.IntegerField(null=False)
    enabler=models.ForeignKey(Enabler,on_delete=models.CASCADE)
    lc=models.ForeignKey(Entity,on_delete=models.CASCADE)
    mc=models.ForeignKey(Entity,on_delete=models.CASCADE)
    tn_fees=models.IntegerField(null=False)
    atom_id = models.ForeignKey(Atom_ID,on_delete=models.CASCADE)
    expa_id = models.ForeignKey(Expa_ID,on_delete=models.CASCADE)
    application_id = models.ForeignKey(Application_ID,on_delete=models.CASCADE)

