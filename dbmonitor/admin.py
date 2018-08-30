from django.contrib import admin

# Register your models here.
from dbmonitor.models import Rule, Query, ExecutionHistory, Connection

admin.site.register(Rule)
admin.site.register(Connection)
admin.site.register(Query)
admin.site.register(ExecutionHistory)
