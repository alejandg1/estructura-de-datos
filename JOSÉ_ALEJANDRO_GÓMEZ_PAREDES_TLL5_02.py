# crear archivo usando/mezclando algunas formas de crearlo

from pathlib import Path

# creando archivo
Fl_Ruta_File = Path("C:/Users/UNEMI/Pictures/Nueva carpeta/Arcivo190523_02.txt")
# escribir contenido

Lv_contenido = ""
Lv_contenido="Esta es mi primera linea de codigo"
Lv_contenido+="Esta es mi segunda linea de codigo"
Lv_contenido+="Esta es mi tercera linea de codigo \ncon salto de linea \n"
# cargando todo en el archivo  ----> transferencia de informaciòn
Fl_Ruta_File.write_text(Lv_contenido)
print("Su cuarto archivo ha sido creado, vamos bien")
