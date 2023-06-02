import  os

Lf_ruta = "C:System_VideoClub"

try:
    os.mkdir(Lf_ruta)
    print("Carpeta creada exitosamente")
except OSError as error:
    print(f"Nose pudo crear la carpeta: {error}")
