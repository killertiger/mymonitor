from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Rule(BaseModel):
    name = models.CharField(max_length=100)
    rule_text = models.CharField(max_length=100)


class Query(BaseModel):
    rule = models.ForeignKey(Rule, on_delete=True)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500)


class ExecutionHistory(BaseModel):
    query = models.ForeignKey(Query, on_delete=True)
    total = models.IntegerField()