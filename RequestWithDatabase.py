import requests 
import json
import time
import psycopg2

def reqF (loc):
    for count in range (5):
        MyUrl = "https://api.openweathermap.org/data/2.5/weather"
        MyParams = {'q' : str(location) , 'appid' : 'fe8a34a39bab345ee66884db604a92a5'}
        response = requests.get(url= MyUrl, params= MyParams ,timeout=3.05)
        data =json.loads(response.text)
        #print(data)
        print ("---------{}---------".format(count))
        print("temp :      {}".format(data['main']['temp']))
        print("humidity :  {}".format(data['main']['humidity']))
        print("time :      {}".format(time.ctime(int(data['dt']))))
        time.sleep(5)

def regDb(city,tem,hud):
    try:
        conn = psycopg2.connect(
        host = '127.0.0.1', #or 'localhost'
        user = 'postgres',
        password = '2727',
        database = 'ashjaeiDb')
        print("Connection to database succeeded...")
    except:
        print("Connection to database failed...")        
        conn.close()
    
    def insert(city,tem,hud):
        try:
            with conn.cursor() as cursor:
                 query = f"""insert into weather values ('{city}','{tem}','{hud}')"""
                 cursor.execute(query)
                 conn.commit()
        finally:
            conn.close()
       

while True :
    location = input('Enter Your City (for exit type end)...: ')
    if location == 'end' :
        break
    print("Location is {}".format(location))
    reqF(location)