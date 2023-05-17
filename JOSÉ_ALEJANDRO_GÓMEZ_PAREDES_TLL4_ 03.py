# escribir archivo desde o en memoria
import io

Fl_Stream = io.StringIO()


Fl_Stream.write("Esta es la primera liena de mi primer archivo"), Fl_Stream.write(
    "Esta es la segunda liena de mi primer archivo\n"
), Fl_Stream.write("Esta es la tercera liena de mi primer archivo con salto de linea"),

## recuperamos la información de la memoria

Lv_información = Fl_Stream.getvalue()

## tranferir informacion a un archivo fisico

with open("Archivo170523_03.txt", "w") as archivo_disco:
    archivo_disco.write(Lv_información)

print("su tercer archivo ha sido creado, vamos bien")

## todo se crea en memoria y luego se guarda en un archivo fisico