import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html

class Komut():
    def __init__(self,gelenSes):
        self.ses = gelenSes.upper()
        self.sesBloklari = self.ses.split()
        print(self.sesBloklari)
        self.komutlar = ["ABONE","CEVİR","NABER","NASILSIN","KAPAT","HAVA"]
    
    #KOMUT VE İŞLEMLERİ 

    def seslendirme(self,yazi):
        tts = gTTS(text=yazi,lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
        print(yazi)
        
    def sohbet(self):
        sozler = ["İyiyim sen nasılsın",
        "Benim duygularım yok ama insanlar sanırım bu soruya iyiyim diye cevap veriyor",
        "Devrelerimi çok iyi hissediyorum :)"
        ]
        secim = choice(sozler)
        self.seslendirme(secim)

    def kapat(self):
        self.seslendirme("Kapatıyorum")
        sys.exit()
    
    def komutBul(self):
        for komut in self.komutlar:
            if komut in self.sesBloklari:
                self.komutCalistir(komut)
    
    def komutCalistir(self,komut):
        if komut == "KAPAT":
            self.kapat()
        if komut == "NEHABER" or komut == "NASILSIN":
            self.sohbet()