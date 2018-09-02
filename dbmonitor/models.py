from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Connection(BaseModel):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    host = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Rule(BaseModel):
    name = models.CharField(max_length=100)
    rule_text = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Query(BaseModel):
    rule = models.ForeignKey(Rule, on_delete=True)
    connection = models.ForeignKey(Connection, null=True, on_delete=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ExecutionHistory(BaseModel):
    query = models.ForeignKey(Query, on_delete=True)
    total = models.IntegerField()


class ExecutionHistoryDetail(BaseModel):
    execution_history = models.ForeignKey(ExecutionHistory, on_delete=True)
    database_name = models.CharField(max_length=100)
    total = models.IntegerField()
