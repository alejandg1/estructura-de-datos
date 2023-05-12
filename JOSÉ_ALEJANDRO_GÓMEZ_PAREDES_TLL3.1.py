Ln_valor=4
Ln_result=Ln_valor%2

if (Ln_result==0):
    print("El número es par")
else:
    print("El número no es par")

print("-----------------------------------------------------")
# indique si es valor es negativo o positivo

Ln_valor=4

if (Ln_valor>0):
    print("El número es positivo")
else:
    print("El número no es negativo")

print("-----------------------------------------------------")
# indique si el valor es par positivo, par negativo, impar negativo o impar positivo

   
if (Ln_result==0):
    if (Ln_valor>0):
        print("El número es par positivo")
    else:
        print("El número es par negativo")
else:
    if (Ln_valor>0):
        print("El número es impar positivo")
    else:
        print("El número es impar negativo")



