from django.http import HttpResponse
from django.shortcuts import render
from .utils import *
from django.template import loader


def index(request):
    template = loader.get_template('qrcode/index.html')
    a = oi()
    context = {
        'ola': a,
    }
    return HttpResponse(template.render(context, request))