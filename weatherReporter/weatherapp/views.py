from django.shortcuts import render
import urllib
import json
# Create your views here.

def home(request):
    return render(request, 'index.html')

def result(request):
    city = request.POST.get('city')
    API_key = "5c5beeac6027c9d894fcf0d9caad9f69"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"


    json_data = urllib.request.urlopen(url).read()
    real_data = json.loads(json_data)

    print(real_data)

    print(f"========================{real_data['coord']['lat']}")

    latituede = real_data['coord']['lat']
    longitude = real_data['coord']['lon']
    main = real_data['weather'][0]['main']
    description = real_data['weather'][0]['description']
    temprature = real_data['main']['temp']
    feels_like = real_data['main']['feels_like']
    humidity = real_data['main']['humidity']

    print (f"this is a data{latituede, longitude, main, description, temprature, feels_like, humidity}")


    context = {
        "latituede" : latituede,
        "longitude" : longitude,
        "main" : main,
        "description" : description,
        "temprature" : temprature,
        "feels_like" : feels_like,
        "humidity" : humidity
    }
    return render(request, 'result.html', context)