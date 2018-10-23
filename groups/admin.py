from django.contrib import admin

# Register your models here.
from groups import models

class GroupMemverInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)