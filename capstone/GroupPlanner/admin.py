from django.contrib import admin
from .models import User, Group, GroupActivities, ActivityStatus

# Register your models here.

admin.site.register(User),
admin.site.register(Group),
admin.site.register(GroupActivities),
admin.site.register(ActivityStatus)

