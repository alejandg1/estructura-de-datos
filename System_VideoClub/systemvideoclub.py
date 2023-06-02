from pathlib import Path
print("Bienvenido al sistema de video club ")
## definiendo ruta
Fl_Ruta_File = Path("C:/System_VideoClub/User_System.txt")
## comprobar exitencia

try:
    Lb_existe = Fl_Ruta_File.exists()

    if(Lb_existe):
        print("File pendiente")

    else:
        print("El sistema no se encuentra instalado de forma corecta, informe a sistemas")
        print("Horario de atencón: Lunes a viernes de 9:00 a 17:00 ")
        print("Telefono: +59399999999");
except IOError as error :
    print(f"no existe información de arranque: {str(error)}")
except Exception as error :
    print(f"Error de las versiones (solicite soporte): {str(error)}")
