import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from komutlar import Komut

r = sr.Recognizer()

while True :#Sonsuz döngü oluşturuyurouz
    with sr.Microphone() as source: #SpeechRecognitiondaki sr ile burda mikrofonu kullanmayı istiyoruz
        #source ilede mikrofondan aldığımız sesi kaydetiyoruz
        print("Birşeyler söyle")
        audio = r.listen(source) 
    
    data = ""
    try :
        data = r.recognize_google(audio, language="tr-tr")
        print(data)
        komut = Komut(data)
        komut.komutBul()
        time.sleep(1)
    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")
