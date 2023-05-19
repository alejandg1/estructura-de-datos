# metodo path de la librerìa pathlib
from pathlib import Path

# creando el archivo junto con la ruta

Fl_Ruta_File = Path("C:/Users/UNEMI/Pictures/Nueva carpeta/Arcivo190523_01.txt")

# obtener ruta general absoluta
Lf_Ruta_Absoluta=Fl_Ruta_File.absolute()
#print(Lf_Ruta_Absoluta)

# verificar si una ruta existe
Lb_Existe = Fl_Ruta_File.exists()
print("¿La ruta existe?::  ", Lb_Existe)

# obtener nombre del archivo


Lf_nombre_file = Fl_Ruta_File.name
print("nombre del archivo: ",Lf_nombre_file)

#obtener la ruta padre/ raiz
print("+++++")

Lf_Ruta_raiz = Fl_Ruta_File.parent
print("El nombre del directorio raiz es: ", Lf_Ruta_raiz)





