import math
Ln_valor=4
Ln_result=Ln_valor%2

#presentar si un número dado es par o impar
if (Ln_result==0):
    print("El número es par")
else:
    print("El número no es par")


print("-----------------------------------------------------")

## recuperar valor entero de un int
Ln_valor =28.129
Ln_parte_entera= int( Ln_valor//1)
print("parte entera recuperada: ",Ln_parte_entera)
print("-----------------------------------------------------")

## recuperar parte decimal de un int
print("recuperando parte decimal")
Ln_parte_decimal= round((Ln_valor%1),2)
print("redondeado: ",Ln_parte_decimal)

print("-----------------------------------------------------")

Ln_parte_decimal= Ln_valor%1
Ln_parte_decimal= '%.3f'%(Ln_parte_decimal)
print("truncado: ",Ln_parte_decimal)


print("-----------------------------------------------------")
Ln_valor=80.1265
print("El número es:", Ln_valor)
Ln_parte_entera,Ln_parte_decimal=math.modf(Ln_valor)

print(f"su parte entera es {round(Ln_parte_entera,4)}, y su parte decimal es: {Ln_parte_decimal}")