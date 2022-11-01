from time import tzname
import pyowm
import tkinter as tk
from tkinter import CENTER, ttk
import urllib.request
from PIL import Image, ImageTk
import pytz
import datetime as dt
import tkinter as tk
from pprint import pprint

owm = pyowm.OWM("--Your API Key--")

wmgr = owm.weather_manager()

wobs = wmgr.weather_at_place("Carindale")
w = wobs.weather



window = tk.Tk()

window.title("Weather (Note that Forecast is in UTC which is -10:00 from AEST)")
window.geometry("800x600")
window.config(bg="white")
window.resizable(False, False)
icon = ImageTk.PhotoImage(file="icon.png")
window.iconphoto(False, icon)

background_image = Image.open("lbackground.png")
background_image = background_image.resize((800, 600))
background_image.save("lbackground.png")

background_image = ImageTk.PhotoImage(file="lbackground.png")

background_label = tk.Label(master=window, image=background_image)
background_label.place(x=0,y=0)

temp_frame = tk.Frame(master=window, width=200, height=580, bg="white", highlightbackground="orange", highlightthickness=3)
temp_frame.pack()
temp_frame.place(x=10, y=10)
temp_frame.pack_propagate(0)

curr_temp = tk.Label(master=temp_frame, text=f"{round(w.temperature('celsius')['temp'])}*C", font="Advance 36", fg="green", bg="white", pady=25)
curr_temp.pack(pady=40)

min_temp = tk.Label(master=temp_frame, text=f"L: {round(w.temperature('celsius')['temp_min'])}*C", font="Advance 12", fg="green", bg="white", pady=25)
min_temp.pack()

min_temp = tk.Label(master=temp_frame, text=f"H: {round(w.temperature('celsius')['temp_max'])}*C", font="Advance 12", fg="green", bg="white", pady=25)
min_temp.pack()

detailedstat = tk.Label(master=temp_frame, text=w.detailed_status, bg="white", fg="black", font="Advance 12 bold", pady=25)
detailedstat.pack()

weather_url = "http://openweathermap.org/img/wn/"+w.weather_icon_name+"@2x.png"

urllib.request.urlretrieve(weather_url, w.weather_icon_name+"@2x.png")
weather_image = ImageTk.PhotoImage(file=w.weather_icon_name+"@2x.png", width=100, height=100)

weather_icon_label = tk.Label(master=temp_frame, image=weather_image, bg="white", padx=25, pady=25)
weather_icon_label.pack()

now = dt.datetime.now()

time = tk.Label(master=window, text=now.time(), fg="Green", width=10, height=10, font="Advance 20")
time.pack()
time.pack_propagate(1)
time.place(x=400, y=300)

#Sunrise
sunrise = str(w.sunrise_time('iso'))
date, time = sunrise.split()
date = date.replace("-", " ")
date = date.split()
time = str(time.replace(":", " "))
time = str(time.replace("+00:00", ""))
time = str(time.replace("+00", ""))
time = time.split()
datetime = dt.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]), tzinfo=pytz.utc)
my_datetime_utc = datetime.strftime('%Y-%m-%d %H:%M:%S')
date, srisetime, tz = str(datetime.astimezone(pytz.timezone('Australia/Brisbane')).strftime('%Y-%m-%d %H:%M:%S %Z%z')).split()
srise_frame = tk.Frame(master=window, bg="white", highlightbackground="orange", highlightthickness=3, width=275, height=100)
srise_frame.pack_propagate(0)
srise_frame.place(x=220, y=10)
sunrise_text = tk.Label(master=srise_frame, text="Sunrise", fg="green", bg="white", highlightbackground="white", highlightthickness=3, font="Avance 24")
sunrise_text.pack()
sunrise = tk.Label(master=srise_frame, text=srisetime, fg="green", bg="white", highlightbackground="white", highlightthickness=3, font="Avance 24")
sunrise.pack()

#Sunset
sunset = str(w.sunset_time('iso'))
date, time = sunset.split()
date = date.replace("-", " ")
date = date.split()
time = str(time.replace(":", " "))
time = str(time.replace("+00:00", ""))
time = str(time.replace("+00", ""))
time = time.split()
datetime = dt.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]), tzinfo=pytz.utc)
my_datetime_utc = datetime.strftime('%Y-%m-%d %H:%M:%S')
date, ssettime, tz = str(datetime.astimezone(pytz.timezone('Australia/Brisbane')).strftime('%Y-%m-%d %H:%M:%S %Z%z')).split()
sset_frame = tk.Frame(master=window, bg="white", highlightbackground="orange", highlightthickness=3, width=275, height=100)
sset_frame.pack_propagate(0)
sset_frame.place(x=510, y=10)
sunset_text = tk.Label(master=sset_frame, text="Sunset", fg="green", bg="white", highlightbackground="white", highlightthickness=3, font="Avance 24")
sunset_text.pack()
sunset = tk.Label(master=sset_frame, text=ssettime, fg="green", bg="white", highlightbackground="white", highlightthickness=3, font="Avance 24")
sunset.pack()

window.mainloop()
