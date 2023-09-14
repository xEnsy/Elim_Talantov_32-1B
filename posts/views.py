from django.shortcuts import HttpResponse
from datetime import datetime
from django.utils.timezone import now
# Create your views here.


def hello(request):
    return HttpResponse("Hello! Its my project")


def now_date(request):
    date = now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"сегодняшняя дата:{date}")


def goodbye(request):
    return HttpResponse("Goodbye user!")


def bruh69(request):
    return HttpResponse("а вы знали что наше сознание бессмертная?")