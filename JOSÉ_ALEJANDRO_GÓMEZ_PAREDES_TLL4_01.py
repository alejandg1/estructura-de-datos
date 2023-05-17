## crear archivo txt

## "w" write sobreescribe archivos existentes eliminando el contenido anterior
## "r" read solo lee
## "a" append
## sin parametro == por defecto usa "r"


Fl_Archivo = open("Archivo170523_01.txt", "a")

## escribir lineas del archivo

Fl_Archivo.write("Esta es la primera liena de mi primer archivo")
Fl_Archivo.write("Esta es la segunda liena de mi primer archivo\n")
Fl_Archivo.write("Esta es la tercera liena de mi primer archivo con salto de linea")


## cerrar archivo

Fl_Archivo.close()

print("Su primer archivo ha sido creado, felicidades")


## crear file consume memoria

## no cerrar  deja procesos huerfano, procesos separados
## no cerrar no permite continuar
