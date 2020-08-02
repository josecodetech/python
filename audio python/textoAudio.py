# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 09:35:16 2020

@author: Jose
"""
from gtts import gTTS

def textoAudio(ficheroTexto, idioma, ficheroAudio):
    with open(ficheroTexto,"r") as fichero:
        texto = fichero.read()
    tts = gTTS(text=texto,lang=idioma)
    tts.save(ficheroAudio)
    print("He terminado de grabar el fichero de audio")

textoAudio("texto.txt","ES","textoAudio.mp3")