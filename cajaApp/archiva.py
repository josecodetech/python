import os
from tkinter import messagebox
def archiva(di,me,an,texto):
    #GUARDAR EN ARCHIVO
    #print('llamada a archivo')
    fecha=str(an)+str(me)+str(di)
    fecha=str(fecha+".txt")
    #print(fecha)
    #print(os.getcwd())    
    try:
        escritura=open(fecha,"w")
        fechaTexto=str(di)+"/"+str(me)+"/"+str(an)+"\n\n"
        escritura.write(fechaTexto)
        escritura.write(texto)
        escritura.close()
    
    except:
        #print("error al archivar")
        textoMensaje="Error al crear archivo"
        messagebox.showinfo("Error",textoMensaje)

def imprime(di,me,an):
    fecha=str(an)+str(me)+str(di)
    fecha=str(fecha+".txt") 
    try:
        os.startfile(fecha, "print")       
    except:
        #print("error al archivar")
        textoMensaje="Error al imprimir archivo"
        messagebox.showinfo("Error",textoMensaje)        
if __name__=='__main__':
    archiva('01','02','19',"hola\ttabulado\nlinea nueva")
    imprime('01','02','19')

