import base64
from _datetime import datetime
import re
from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the location records index.")


def save_record(request, encode_params):
    param_str = base64.standard_b64decode(encode_params.encode())
    param_list = param_str.decode().split(',')
    record = models.LocationRecords()
    record.imei = param_list[0]
    record.longitude = param_list[1]
    record.latitude = param_list[2]
    record.update_time = datetime.fromtimestamp(int(param_list[3])/1000)
    record.save()
    print(param_list)
    return HttpResponse("success")

