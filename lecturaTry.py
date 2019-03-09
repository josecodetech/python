#Nos aseguramos que no de error
try:
   f = open("fichero.txt")
   print(f.read())
   print('fichero correcto')
finally:
   f.close()