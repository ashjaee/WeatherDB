import requests 
import json

MyUrl = "https://api.openweathermap.org/data/2.5/weather"
MyParams = {'q' : 'tehran' , 'appid' : 'fe8a34a39bab345ee66884db604a92a5'}
print('fsdssd')
response = requests.get(url= MyUrl, params= MyParams )

data =json.loads(response.text)
print(data)


        