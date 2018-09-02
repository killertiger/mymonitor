from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from dbmonitor.business import ValidatorBusiness
from dbmonitor.models import Query, ExecutionHistory


def index(request):
    queries = Query.objects.filter(is_active=True)
    queries_succeed = []
    queries_failed = []

    for query in queries:
        history = ExecutionHistory.objects.filter(query=query).order_by('-created_date').first()
        if history:
            if history.total == 0:
                queries_succeed.append(history)
            else:
                queries_failed.append(history)

    template = loader.get_template('dbmonitor/index.html')
    context = {
        'queries_succeed': queries_succeed,
        'queries_failed': queries_failed,
    }

    return HttpResponse(template.render(context, request))


def run_all_validators(request):
    validator = ValidatorBusiness()
    validator.validate_all_monitors()

    return HttpResponse("OK")

