from djitellopy import Tello
import speech_recognition as sr
#from gtts import gTTS 

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
except sr.UnknownValueError:
   print("Bir daha söyler misin?")
   
tello = Tello()

tello.connect()


if data == "havalan":
   tello.takeoff()
if data == "sola":
   tello.move_left(100)
if data == "sağa":
   tello.move_right(100)
if data == "ileri":
   tello.move_forward(100)
if data == "saat yönü":   
   tello.rotate_clockwise(90)

tello.land()
