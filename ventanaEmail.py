from tkinter import *
from tkinter import messagebox
import smtplib
def enviar():
    email=emailDestino.get()
    texto=text.get(1.0,END)
    remitente='dafsdafa@gmail.com' #cambiado por seguridad
    destinatario=email
    msg=texto
    username='dafsdafa@gmail.com'#cambiado por seguridad
    password='pdfafsafsa'#cambiado por seguridad
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(remitente,destinatario,msg)
    server.quit()
    messagebox.showinfo("Mensaje","Email enviado")
def borrar():
    emailDestino.set("")
    text.delete(1.0,END)
    
                        
ANCHO=740
ALTO=550

ventana=Tk()
anchoAlto=str(ANCHO)+"x"+str(ALTO)
ventana.geometry(anchoAlto)
ventana.title("Envia email")
colorFondo="#007"
colorLetra="#FFF"
ventana.configure(background=colorFondo)
emailDestino=StringVar()
etiquetaEmail=Label(ventana,text="Email",bg=colorFondo,fg=colorLetra).place(x=50,y=40)
cajaEmail=Entry(ventana,textvariable=emailDestino).place(x=110,y=40,width=180)
etiquetaTexto=Label(ventana,text="Texto",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
text=Text(ventana)
text.place(x=110,y=80,width=500)
botonEnviar=Button(ventana,text="Enviar",command=enviar,bg=colorFondo,fg=colorLetra).place(x=270,y=500)
botonBorrar=Button(ventana,text="Borrar",command=borrar,bg=colorFondo,fg=colorLetra).place(x=330,y=500)
mainloop()

