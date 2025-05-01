from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    print("Delhi.")
    try:
        city = textfield.get()

        # Validate if city name is entered
        if not city:
            messagebox.showerror("Weather App", "Please enter a city name.")
            return

        # Geo Locator
        # geolocator = Nominatim(user_agent="geoapiExercises")
        # location = geolocator.geocode(city)
        geolocator = Nominatim(user_agent="my-weather-app")
        try:
            location = geolocator.geocode(city, timeout=10)
        except Exception as e:
            messagebox.showerror("Weather App", f"Geolocation error: {e}")
            return


        if location is None:
            messagebox.showerror("Weather App", "City not found. Please enter a valid city.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lat=location.latitude, lng=location.longitude)
        print("Delhi..")

        if result is None:
            messagebox.showerror("Weather App", "Timezone not found for the city.")
            return

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="Current Weather")
        print("Delhi...")

        # Weather API
        api_key = "8623a3797a46ab4d79e4edcdfd845b3a"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        print("Delhi....")
        
        json_data = response.json()

        print("URL:", url)
        print("Response Status:", response.status_code)
        print("Response JSON:", json_data)

        print("Delhi.....")

        if json_data.get("cod") != 200:
            messagebox.showerror("Weather App", json_data.get("message", "Weather data not found."))
            return
        print("Delhi6")

        # Extract weather details
        condition_now = json_data['weather'][0]['main']
        description_now = json_data['weather'][0]['description']
        temperature_now = int(json_data['main']['temp'])
        wind_now = json_data['wind']['speed']
        humidity_now = json_data['main']['humidity']
        pressure_now = json_data['main']['pressure']

        # Update UI
        temp.config(text=(temperature_now, "°C"))
        condition_lbl.config(text=(condition_now, "|", "Feels like", temperature_now, "°C"))
        wind.config(text=wind_now)
        humidity.config(text=humidity_now)
        description.config(text=description_now)
        pressure.config(text=pressure_now)

    except Exception as e:
        messagebox.showerror("Weather App", f"Error: {str(e)}")


# search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# button box
frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# labels
Label1 = Label(root, text="WIND", font=("poppins", 15, "bold"), bg="#1ab5ef", fg="white")
Label1.place(x=120, y=400)

Label2 = Label(root, text="HUMIDITY", font=("poppins", 15, "bold"), bg="#1ab5ef", fg="white")
Label2.place(x=250, y=400)

Label3 = Label(root, text="DESCRIPTION", font=("poppins", 15, "bold"), bg="#1ab5ef", fg="white")
Label3.place(x=420, y=400)

Label4 = Label(root, text="PRESSURE", font=("poppins", 15, "bold"), bg="#1ab5ef", fg="white")
Label4.place(x=600, y=400)

temp = Label(font=("arial", 70, "bold"), fg="#ee666d")
temp.place(x=400, y=150)
condition_lbl = Label(font=("arial", 15, "bold"))  # renamed from "condition" to "condition_lbl"
condition_lbl.place(x=400, y=250)

wind = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
wind.place(x=120, y=430)
humidity = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
humidity.place(x=250, y=430)
description = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
description.place(x=420, y=430)
pressure = Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
pressure.place(x=600, y=430)

root.mainloop()