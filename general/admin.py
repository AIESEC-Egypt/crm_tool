from django.contrib import admin
from general.models import *
from opportunities.models import *
from tm.models import *

# Register your models here.

admin.site.register(Entity)
admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Background)
admin.site.register(Department)
admin.site.register(Address)
admin.site.register(Tag)
admin.site.register(Opportunity)
admin.site.register(Slot)
admin.site.register(TouchPoints)
admin.site.register(OperationalGoal)