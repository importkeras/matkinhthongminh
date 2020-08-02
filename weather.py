import requests
from pprint import pprint
from googletrans import Translator
from gtts import gTTS 
import os 

translator = Translator()
weatherData = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + "5f0736542e1606c9872f4f3e4703fdd7" + "&q=" + "Da Nang").json()
result = translator.translate(weatherData["weather"][0]["description"], src = "en", dest = "vi")
speech = gTTS(text = "Thời tiết hiện tại là " + result.text + " nhiệt độ là " + str(int(weatherData["main"]["temp"] // 10)) + " độ xê độ ẩm là " + str(int(weatherData["main"]["humidity"])) + " phần trăm", lang = "vi", slow = False) 
speech.save("quochuy.mp3") 
os.system("quochuy.mp3")