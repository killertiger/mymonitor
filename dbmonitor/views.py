from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from dbmonitor.business import ValidatorBusiness
from dbmonitor.models import Query, ExecutionHistory


def index(request):
    queries = Query.objects.all()
    history_list = []
    for query in queries:
        history = ExecutionHistory.objects.filter(query=query).order_by('-created_date').first()
        history_list.append(history)

    template = loader.get_template('dbmonitor/index.html')
    context = {
        'history_list': history_list,
    }

    return HttpResponse(template.render(context, request))


def run_all_validators(request):
    validator = ValidatorBusiness()
    validator.validate_all_monitors()

    return HttpResponse("OK")

