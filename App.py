import tkinter as tk # tkinter in Python's native GUI library
import GetIcon # importing and executing the GetIcon.py file's code
from tkinter import font # tkinter's libarary for fonts 
import requests # pip's Requests package to talk to API's
from PIL import Image, ImageTk # pip Pillow libarary to display the weather icons

# setting default values
HEIGHT = 400
WIDTH = 650
PRIMARYBG = '#333'
SECONDARYBG = '#222'
TERNARYBG = '#777'
FONT = 'Courier'
PLACEHOLDER = 'enter the city...'

# function to remove text presnet in the entry field
def userText(event):
    entry.delete(0,len(PLACEHOLDER))
    usercheck=True

# function to display weather icon
def AddIcon(icon):
    size = int(lowerFrame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./assests/icons/'+icon+'.png').resize((size, size)))
    weatherIcon.delete("all")
    weatherIcon.create_image(0,0, anchor='nw', image=img)
    weatherIcon.image = img

# function to format and display the json data
def FormatWeather(weather):
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

# function to make API call to openweathermap.org's server and parse the result
def GetWeather(city):
    try:
        if(city in [PLACEHOLDER, '']):
            label['text'] = 'Enter valid city!'
        else:
            weatherKey = 'abb705b631f4e41f616a406fcb10579b'
            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'APPID': weatherKey, 'q':city, 'units': 'imperial'}
            response = requests.get(url, params=params)
            weather = response.json()
            label['text'] = FormatWeather(weather)
    except:
        label['text'] = 'RIP!'

# root
root = tk.Tk()
root.minsize(height=HEIGHT, width=WIDTH)
root.maxsize(height=HEIGHT+100, width=WIDTH+200)
root.title("Dark Weather")
root.iconbitmap(r'./assests/logo.ico')

# canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=PRIMARYBG)
canvas.pack(fill='both', expand=True)

# upper frame housing entry and button
upperFrame = tk.Frame(root, bg=SECONDARYBG, bd=5)
upperFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry widget to enter city name
entry = tk.Entry(upperFrame, bg=TERNARYBG, font=(FONT, 12), borderwidth=5, relief=tk.FLAT)
entry.place(relwidth=0.65, relheight=1)
entry.insert(0, PLACEHOLDER)
entry.bind("<Button>",userText)

# button widget to call actions
button = tk.Button(upperFrame, text="Get Weather", bg=TERNARYBG, font=(FONT, 12), command=lambda: GetWeather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# lower frame housing label and weahterIcon
lowerFrame = tk.Frame(root, bg=SECONDARYBG, bd=5)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label widget to display all the parsed weather data
label = tk.Label(lowerFrame, text='...', bg=TERNARYBG, font=(FONT, 12), bd=5)
label.place(relwidth=1, relheight=1)

# canvas used to display weather icon
weatherIcon = tk.Canvas(lowerFrame, bg=TERNARYBG, bd=5, highlightthickness=0)
weatherIcon.place(relx=.85, rely=0.01, relwidth=0.15, relheight=0.3)

root.mainloop() # runs the application