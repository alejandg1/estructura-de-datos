# crear archivo
# "as" asigna un "alias"
with open("Archivo170523_02.txt", "w") as File01:
    File01.write("Esta es la primera liena de mi primer archivo")
    File01.write("Esta es la segunda liena de mi primer archivo\n")
    File01.write("Esta es la tercera liena de mi primer archivo con salto de linea")

    ## no se debe cerrar
    print("su segundo archivo ha sido creado, vamos bien.")

# usando with se tiene la certeza de que se cierra
