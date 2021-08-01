import speech_recognition as sr
import os
import webbrowser

r = sr.Recognizer()
with sr.Microphone() as source:
     print("Benimle Konuş!")
     audio = r.listen(source)
data = ""
try:
   data = r.recognize_google(audio, language='tr-tr')
   data = data.lower()
   print("Söylenilen:" + data)
   finaldata = data.split()
   finaldata = data.strip()
except sr.UnknownValueError:
   print("Bir daha söyler misin?")
   
if data == "youtube":
   url2 = 'https://www.youtube.com'
   webbrowser.open(url2)
   
elif data == "sahibinden":
   url3 = 'https://www.sahibinden.com'
   webbrowser.open(url3)

if data == "bilgisayarı kapat":
    os.system('shutdown -s')
    
if data == "reset at":    
    os.system("shutdown -r -t 1")
