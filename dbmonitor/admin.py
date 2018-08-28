from django.contrib import admin

# Register your models here.
from dbmonitor.models import Rule, Query

admin.site.register(Rule)
admin.site.register(Query)
