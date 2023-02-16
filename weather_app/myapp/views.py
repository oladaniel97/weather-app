from django.shortcuts import render, redirect
import requests
import json
import datetime
from .models import City
from .forms import cityform

# Create your views here.
def index(request):
    if request.method == 'POST':
        form  = cityform(request.POST)
        form.save()

    form = cityform()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
       
        api_my = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=fd917a564e2a127eb9abf3b5b98603c1".format(city)).json()
        
    #     unx = api_my['sys']['sunrise']
    #     unxs = api_my['sys']['sunset']
    #     date_times = datetime.datetime.fromtimestamp(unxs)
    #     date_time = datetime.datetime.fromtimestamp(unx)
    #     print("Date & Time =>" ,
    # date_time.strftime('%Y-%m-%d %H:%M:%S'))
    #     print(api_my)

        data = {
            'id': id,
            'city': city.name,
            'weather_description': api_my['weather'][0]['description'],
            'weather_temp': api_my['main']['temp'],
            'weather_pressure': api_my['main']['pressure'],
            'weather_humidity': api_my['main']['humidity'],
            'weather_icon': api_my['weather'][0]['icon'],
            'country': api_my['sys']['country'],
            # 'sunrise': date_time.strftime('%H:%M:%S'),
            # 'sunset': date_times.strftime('%H:%M:%S')
        }
        weather_data.append(data)

        if city is  weather_data:
            pass



    return render(request, 'index.html', {'weather_data':weather_data,'form':form})

def delete(request, city):
    pos=City.objects.get(name=city)
    pos.delete()
    
    
    return redirect('/?id=0')
