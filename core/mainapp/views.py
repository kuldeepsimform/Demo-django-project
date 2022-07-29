from django.shortcuts import render
from django.http import HttpResponse
from .tasks import task_func

# Create your views here.

def test(reuqest):
    task_func.delay()
    return HttpResponse("Done")