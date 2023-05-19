from pathlib import Path
# creando archivo
Fl_Ruta_File = Path("C:/Users/UNEMI/Pictures/Nueva carpeta/Arcivo190523_04.txt")
# combinar funciones y procesos
#1.  preguntar si existe  la ruta antes del archivo
# cramos una estructura de control para los errores
Lb_existe_root = Fl_Ruta_File.parent.exists()


try:
    if Lb_existe_root:
        Lb_existe_File=Fl_Ruta_File.exists()
        if Lb_existe_File:
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
                    Archivo.write("Esta es mi primera linea del 6to archivo")
                    
                    Archivo.write("Esta es mi tercera linea del 6to archivo\n")
                    Archivo.write("Esta es mi tercera linea del 6to archivo con salto de linea\n")

                print("su 6to archivo ha sido creado")

            elif(Lv_opcion=="n" or Lv_opcion =="N"):
                print("Proceso terminado")

            else:
                print("opcion invalidaa")
    else:
        print("La ruta especifica no existe, contacte al area de sistemas")
except IOError as Error:
    print("Nose puede crear el File: ",str(Error))
    #error en la escritura
except Exception  as  Error:
    print("Nose puede crear el File: ",str(Error))
    #nadei sabe lo que ocurriò