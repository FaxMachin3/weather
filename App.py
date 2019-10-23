# GUI: 
import tkinter as tk
import GetIcon
from tkinter import font
import requests
from PIL import Image, ImageTk

HEIGHT = 400
WIDTH = 650
PRIMARYBG = '#333'
SECONDARYBG = '#222'
TERNARYBG = '#777'
FONT = 'Courier'
PLACEHOLDER = 'enter the city...'

def userText(event):
    entry.delete(0,len(PLACEHOLDER))
    usercheck=True

def AddIcon(icon):
    size = int(lowerFrame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weatherIcon.delete("all")
    weatherIcon.create_image(0,0, anchor='nw', image=img)
    weatherIcon.image = img


def FormateWeather(weather):
    try:
        city = weather['name']
        desc = weather['weather'][0]['description']
        tempF = round(weather['main']['temp'], 1)
        tempC = round((tempF - 32) / 1.8, 1)
        icon = weather['weather'][0]['icon']
        AddIcon(icon)
        return 'City: %s \nDescription: %s \nTemperature (°F/°C): %s / %s' % (city, desc, tempF, tempC)
    except:
        return 'Sorry! The was a problem retrieving information.'

def GetWeather(city):
    try:
        print(city)
        if(city in [PLACEHOLDER, '']):
            label['text'] = 'Enter valid city!'
        else:
            weatherKey = 'abb705b631f4e41f616a406fcb10579b'
            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'APPID': weatherKey, 'q':city, 'units': 'imperial'}
            response = requests.get(url, params=params)
            weather = response.json()
            label['text'] = FormateWeather(weather)
    except:
        label['text'] = 'RIP!'

root = tk.Tk()
root.minsize(height=HEIGHT, width=WIDTH)
root.maxsize(height=HEIGHT+100, width=WIDTH+200)
root.title("Dark Weather")
root.iconbitmap(r'./assests/sun_icon.ico')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=PRIMARYBG)
canvas.pack(fill='both', expand=True)

upperFrame = tk.Frame(root, bg=SECONDARYBG, bd=5)
upperFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(upperFrame, bg=TERNARYBG, font=(FONT, 12), borderwidth=5, relief=tk.FLAT)
entry.place(relwidth=0.65, relheight=1)
entry.insert(0, PLACEHOLDER)
entry.bind("<Button>",userText)

button = tk.Button(upperFrame, text="Get Weather", bg=TERNARYBG, font=(FONT, 12), command=lambda: GetWeather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)
# root.bind('<Return>', lambda event, x=entry.get(): GetWeather(x))

lowerFrame = tk.Frame(root, bg=SECONDARYBG, bd=5)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame, text='...', bg=TERNARYBG, font=(FONT, 12), bd=5)
label.place(relwidth=1, relheight=1)

weatherIcon = tk.Canvas(lowerFrame, bg=TERNARYBG, bd=5, highlightthickness=0)
weatherIcon.place(relx=.85, rely=0.01, relwidth=0.15, relheight=0.3)

root.mainloop()