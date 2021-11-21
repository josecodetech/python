import qrcode

nombreArchivo = input("Dime el nombre del archivo sin la extension ")
textoQr = input("Dime el texto o enlace para el codigo QR ")

imagen = qrcode.make(textoQr)
fichero = open(nombreArchivo+".png", "wb")
imagen.save(fichero)
fichero.close()
print("El codigo QR ha sido generado con exito")
print("El archivo esta guardado en la carpeta del script")
