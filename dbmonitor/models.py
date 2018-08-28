from django.db import models


class Rule(models.Model):
    name = models.CharField(max_length=100)
    rule_text = models.CharField(max_length=100)


class Query(models.Model):
    rule = models.ForeignKey(Rule, on_delete=True)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
