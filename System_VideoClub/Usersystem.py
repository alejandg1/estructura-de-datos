## conjuntos
from pathlib import Path
Cj_Usuarios={
"Usuario1":{
"nombre":"Alejandro Gómez",
"Clave":"ABD",
"rol":"Administrador",
"fechaingreso":"2023-06-02"
},
"Usuario2":{
"nombre":"Adre",
"Clave":"12334241565",
"rol":"analista",
"fechaingreso":"2023-06-06"


},
"Usuario3":{
"nombre":"Mika noir",
"Clave":"loki",
"rol":"Cliente",
"fechaingreso":"2023-06-02"
}
}


Fl_ruta=Path("C:/System_VideoClub/User_System.txt")

with Fl_ruta.open (mode="w") as archivoUser:
    for usuarios, datos in Cj_Usuarios.items():
        line = f"{usuarios}\n"
        for clave,valor in datos.items():
            line+= f"{clave}={valor}\n"
        line=line.rstrip(",")+"\n"
        archivoUser.write(line)