from django.shortcuts import render
from light_power.models import power
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Welcome to street_light_api")

def add_to_database(request, power_usage):
    power_con = power.objects.create(power_consumption=power_usage)
    power_con.save()
    data={'Power Consumption':power_usage}
    return JsonResponse(data)

def display(request):
    power_data = list(power.objects.values('id', 'date_time_record', 'power_consumption'))
    # power_data = power.objects.all()
    data=dict()
    for item in power_data:
        # a = item.power_consumption
        # b = str(item.date_time_record
        # c = str(item.id)
        a=item['power_consumption']
        b=str(item['date_time_record'])[:19]
        c=str(item['id'])
        data[c]={
            b:a,
        }
    # return render(request, 'light_power/display.html',context=data)
    return JsonResponse(data,safe=False)
