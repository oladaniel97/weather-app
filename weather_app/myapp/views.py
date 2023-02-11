from django.shortcuts import render
import urllib
import json
import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        
        city = request.POST.get('city')
        my_api = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ city +"&units=metric&APPID=fd917a564e2a127eb9abf3b5b98603c1").read()
        api_my = json.loads(my_api)
        unx = api_my['sys']['sunrise']
        unxs = api_my['sys']['sunset']
        date_times = datetime.datetime.fromtimestamp(unxs)
        date_time = datetime.datetime.fromtimestamp(unx)
        print("Date & Time =>" ,
      date_time.strftime('%Y-%m-%d %H:%M:%S'))
        print(api_my)

        data = {
            'city': city,
            'weather_description': api_my['weather'][0]['description'],
            'weather_temp': api_my['main']['temp'],
            'weather_pressure': api_my['main']['pressure'],
            'weather_humidity': api_my['main']['humidity'],
            'weather_icon': api_my['weather'][0]['icon'],
            'country': api_my['sys']['country'],
            'sunrise': date_time.strftime('%H:%M:%S'),
            'sunset': date_times.strftime('%H:%M:%S')
        }
        
   


    else:
        
        data = {
            
        }
    return render(request, 'index.html', {'data':data})
