
from pathlib import Path

# creando archivo


Fl_Ruta_File = Path("C:/Users/UNEMI/Pictures/Nueva carpeta/Arcivo190523_03.txt")

# combinar funciones y procesos
#1.  preguntar si existe el FILE

Lb_existe = Fl_Ruta_File.exists()

if(Lb_existe):
    #abrir y leer el archivo 
    with Fl_Ruta_File.open(mode="r") as Archivo :
        for line in Archivo:
            print(line)
        print("fin del archivo existente")

else:

    print("El archino no existe, ¿Desea crearlo?")
    Lv_opcion=input(">>")
    if(Lv_opcion=="s" or Lv_opcion=="S"):
        # crear archivo
        # abrir y escribir en el archivo
        with Fl_Ruta_File.open(mode="w") as Archivo:
            Archivo.write("Esta es mi primera linea del 5to archivo")
            Archivo.write("Esta es mi tercera linea del 5to archivo\n")
            Archivo.write("Esta es mi tercera linea del 5to archivo con salto de linea\n")

    elif(Lv_opcion=="n" or Lv_opcion =="N"):
        print("Proceso terminado")

    else:
         print("opcion invalidaa")


    