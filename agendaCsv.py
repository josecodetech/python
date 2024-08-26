# -*-coding:utf-8 -*-

"""
Created on Fri Dic 06 07:48:08 2019

@author: Jose
"""

#modulos
import csv
import itertools
import re

#clases
class Contacto:
    nuevoId=itertools.count()
    def __init__(self,nombre,apellidos,empresa,fijo,movil):
        self.codigo=next(self.nuevoId)
        self.nombre=nombre
        self.apellidos=apellidos
        self.empresa=empresa
        self.fijo=fijo
        self.movil=movil
class Agenda:
    def __init__(self):
        self.contactos=[]
    def ordenarNombre(self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)
    def ordenarApellidos(self):
        self.contactos.sort(key=lambda contacto: contacto.apellidos)
    def añadir(self,nombre,apellidos,empresa,fijo,movil):
        contacto=Contacto(nombre,apellidos,empresa,fijo,movil)
        self.contactos.append(contacto)
    def mostrarTodos(self):
        self.submenuOrden()
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
    def buscar(self,textoBuscar):
        encontrado=0
        for contacto in self.contactos:
            if(re.findall(textoBuscar,contacto.nombre)) or (re.findall(textoBuscar,contacto.apellidos)):
                self.imprimeContacto(contacto)
                encontrado=encontrado+1
                self.submenuBuscar(contacto.codigo)
        if encontrado==0:
            self.noEncontrado()
    def borrar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                print('---*---*---*---*---*---*---*---*')
                print('Quieres borrarlo? (s/n)')
                print('---*---*---*---*---*---*---*---*')
                opcion=str(input(""))
                if opcion=='s' or opcion=='S':
                    print('Borrando contacto!!!')
                    del self.contactos[codigo]
                elif opcion=='n' or opcion=='N':
                    break
    def modificar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                del self.contactos[codigo]
                nombre=str(input('Escribe el nombre: '))
                apellidos=str(input('Escribe los apellidos: '))
                empresa=str(input('Escribe la empresa: '))
                fijo=str(input('Escribe el fijo: '))
                movil=str(input('Escribe el movil: '))
                contacto=Contacto(nombre.capitalize(),apellidos.capitalize(),empresa.capitalize(),fijo,movil)
                self.contactos.append(contacto)
                break
    def submenuBuscar(self,codigo):
        print('---*---*---*---*---*---*---*---*')
        print('Quieres (m)odificarlo o (b)orrarlo? ')
        print('---*---*---*---*---*---*---*---*')
        opcion=str(input(""))
        if opcion=='m' or opcion=='M':
            self.modificar(codigo)
        elif opcion=='b' or opcion=='B':
            self.borrar(codigo)
        else:
            print('Continuamos sin realizar modificacion alguna')
    def submenuOrden(self):
        print('---*---*---*---*---*---*---*---*')
        print('Quieres ordenar por (n)ombre o por (a)pellidos?')
        print('---*---*---*---*---*---*---*---*')
        opcion=str(input(""))
        if opcion=='n' or opcion=='N':
            self.ordenarNombre()
        elif opcion=='a' or opcion=='A':
            self.ordenarApellidos()

    def grabar(self):
        with open('agenda.csv','w') as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(('codigo','nombre','apellidos','empresa','fijo','movil'))
            for contacto in self.contactos:
                escribir.writerow((contacto.codigo,contacto.nombre,contacto.apellidos,contacto.empresa,contacto.fijo,contacto.movil))
    def imprimeContacto(self,contacto):
        print('---*---*---*---*---*---*---*---*')
        print('---*---*---*---*---*---*---*---*')
        print('Codigo: {}'.format(contacto.codigo))
        print('Nombre: {}'.format(contacto.nombre))
        print('Apellidos: {}'.format(contacto.apellidos))
        print('Empresa: {}'.format(contacto.empresa))
        print('Fijo: {}'.format(contacto.fijo))
        print('Movil: {}'.format(contacto.movil))        
        print('---*---*---*---*---*---*---*---*')
        print('---*---*---*---*---*---*---*---*')
    def noEncontrado(self):
        print('---*---*---*---*---*---*---*---*')
        print('---*---*---*---*---*---*---*---*')
        print('Contacto no encontrado')
        print('---*---*---*---*---*---*---*---*')
        print('---*---*---*---*---*---*---*---*')
def ejecutar():
    agenda=Agenda()
    try:
        with open('agenda.csv','r') as fichero:
            lector=csv.DictReader(fichero,delimiter=',')
            for fila in lector:
                agenda.añadir(fila['nombre'].capitalize(),fila['apellidos'].capitalize(),fila['empresa'].capitalize(),fila['fijo'].capitalize(),fila['movil'].capitalize())
    except:
        print('Error al abrir fichero o que no existe aun')
    while True:
        menu=str(input("""
        \nSelecciona una opcion\n
        1 Mostrar lista de contactos
        2 Buscar contacto
        3 Añadir contacto
        0 Salir \n\n               
        """))
        if menu=='1':
            agenda.mostrarTodos()
        elif menu=='2':
            texto=str(input('Escribe el texto a buscar en contactos: '))
            agenda.buscar(texto.capitalize())
            agenda.grabar()
        elif menu=='3':
            nombre=str(input('Escribe el nombre: '))
            apellidos=str(input('Escribe los apellidos: '))
            empresa=str(input('Escribe la empresa: '))
            fijo=str(input('Escribe el fijo: '))
            movil=str(input('Escribe el movil: ')) 
            agenda.añadir(nombre.capitalize(),apellidos.capitalize(),empresa.capitalize(),fijo,movil)
            agenda.grabar()
        elif menu=='0':
            print('Hasta pronto!!!')
            agenda.grabar()
            break
        else:
            print('Opcion no valida!!!')
if __name__=='__main__':
    ejecutar()
        