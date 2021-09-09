import requests 
import json
import time
import psycopg2

def reqF (loc,loop):
    for count in range (loop):
        MyUrl = "https://api.openweathermap.org/data/2.5/weather"
        MyParams = {'q' : str(location) , 'appid' : 'fe8a34a39bab345ee66884db604a92a5'}
        response = requests.get(url= MyUrl, params= MyParams ,timeout=10)
        data =json.loads(response.text)
        print('---',str(count+1),'/',str(loop),'---  registed...')
        time.sleep(2)
        regDb(location,data['main']['temp'],data['main']['humidity'])

def regDb(city,tem,hud):
    try:
        conn = psycopg2.connect(
        host = '127.0.0.1', #or 'localhost'
        user = 'postgres',
        password = '2727',
        database = 'ashjaeiDb')
        #print("Connection to database succeeded...")
        with conn.cursor() as cursor:
            query = """insert into weather values ('{}',{},{})""".format(city,tem,hud)
            cursor.execute(query)
            conn.commit()
    except:
        print("Connection to database failed...")        
        conn.close()
    
while True :
    location = input('Enter Your City (for exit type end)...: ')
    if location == 'end' :
        break
    loop = input('Enter Your count ...: ')
    reqF(location,int(loop))