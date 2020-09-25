import speech_recognition as sr
#from gtts import gTTS 
import os
#from googletrans import Translator
import webbrowser

#Recognizer -> r
r = sr.Recognizer()
with sr.Microphone() as source:
     print("Benimle Konuş!")
     audio = r.listen(source)
#Tanıdıktan sonra eğer dediğiniz şey boş bir ses değilse, yani tıkırtı vs. Dediğiniz geri döndürecek.
data = " "
try:
   data = r.recognize_google(audio, language='tr-tr')
   data = data.lower()
   print("Söylenilen : " + data)
   #tts = gTTS(data + "işlem gerçekleştiriliyor", lang='tr',slow = False)
   #tts.save("new.mp3") 
   #os.system("new.mp3")
   finaldata = data.split()
except sr.UnknownValueError:
   print("Bir daha söyler misin?")
   
if data == "youtube aç":
   url2 = "https://www."+str(finaldata[0])+".com/"
   webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
   webbrowser.get('chrome').open_new(url2)

elif finaldata[1] == "gönder":
   url = "https://www."+str(finaldata[0])+".com/"
   webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
   webbrowser.get('chrome').open_new(url)      
   
if data == "sahibinden":
   url3 = 'https://www.sahibinden.com'
   webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
   webbrowser.get('chrome').open_new(url3)
   
elif data == "sahibinden hyundai accent":
   url4 = 'https://www.sahibinden.com/vasita?query_text_mf=hyundai+accent&query_text=hyundai+accent'
   webbrowser.register('chrome',None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
   webbrowser.get('chrome').open_new(url4)

if data == "call of":
   os.system("CoDMP.exe")

if data == "bilgisayarı kapat":
    os.system('shutdown -s')
    
if data == "reset at":    
    os.system("shutdown -r -t 1")


