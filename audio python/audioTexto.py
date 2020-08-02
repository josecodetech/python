# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:29:45 2020

@author: Jose
"""

import speech_recognition as sr

r = sr.Recognizer()
#desde microfono
with sr.Microphone() as recurso:
    print("Dime algo ... ")
    audio = r.listen(recurso)
    try:
      texto = r.recognize_google(audio,language='es-ES')
      print("Esto es lo que has dicho : {}".format(texto))
      with open("audio.wav","wb") as fichero:
          fichero.write(audio.get_wav_data())
    except:
        print("Lo siento no te entendi")
#desde fichero audio
import time
with sr.AudioFile("audio.wav") as recurso:
    audio = r.listen(recurso)
    try:
        print("Leyendo fichero de audio...")
        texto = r.recognize_google(audio,language='es-ES')
        time.sleep(0.5)
        print(texto)
    except:
        print("Lo siento ha ocurrido un error")