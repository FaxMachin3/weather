import os # used for operating system related functionality
import urllib.request # used to make API call to openweathermap.org's server to get weather icons

# mapping for the weather icons
day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

baseUrl = 'https://openweathermap.org/img/w/'
imgDir = './assests/icons/'
if not os.path.exists(imgDir):
	os.makedirs(imgDir)

# Get the day weather icons
for name in day:
	fileName = imgDir+name
	if not os.path.exists(fileName):
		urllib.request.urlretrieve(baseUrl+name, fileName)

# Repeat the same thing for night weather icons
for name in night:
	fileName = imgDir+name
	if not os.path.exists(fileName):
		urllib.request.urlretrieve(baseUrl+name, fileName)