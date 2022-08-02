from django.shortcuts import render
from django.http import HttpResponse

from app_two.models import AccessRecord

# Create your views here.


def index(request):
    webpages = AccessRecord.objects.order_by('date')
    acc_dict = {'acc_rec':webpages}
    return render(request, 'app_two/index.html', context=acc_dict)


def help(request):
    help_dict = {'name': "Help page"}
    return render(request, 'app_two/help.html', context=help_dict)
