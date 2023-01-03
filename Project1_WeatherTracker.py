#Name: Cole Branston
#Date: 2002/07/23
#Purpose: Creat a program that can tell you what the weather is 

import requests
import os
from datetime import datetime

again = "Y"

while again == "Y":

    try:

        user_api = os.environ['current_weather_data']
        location = input("\nEnter the city name: ")

        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        #create variables to store and display data
        temp_city = ((api_data['main']['temp']) - 273.15)
        min_temp = round(((api_data['main']['temp_min']) - 273.15))
        max_temp = round(((api_data['main']['temp_max']) - 273.15))
        feels_like = round(((api_data['main']['feels_like']) - 273.15))
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        longitude = api_data['coord']['lon']
        latitude = api_data['coord']['lat']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        

        print ("\n-----------------------------------------------------------------")
        print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        print ("-------------------------------------------------------------------")

        print ("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
        print("min temp              :",min_temp, "deg C")
        print("max temp              :",max_temp, "deg C")
        print("Feels like            :",feels_like, "deg C")
        print ("Current weather desc  :",weather_desc)
        print ("Current Humidity      :",hmdt, '%')
        print ("Current wind speed    :",wind_spd ,'kmph')
        print("Coordinates           :", str(latitude)+",", longitude)
        print()
        again = input("Do you want to restart the program (Y/N): ").upper()

    except:
        print("\n-----------------------------------------------")
        print("Sorry there has been an error, please try again")
        print("-------------------------------------------------")
        continue

    