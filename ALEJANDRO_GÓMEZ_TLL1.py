import math

# estandares de variables:
# Lv = local varchar
# Ln = local numerica
# Lf local float
# Ld local double
# Lc local decimal
# Gv global varchar  

Lv_Cadena1 = "Hola mundo"
Lv_Cadena2= 'hola mundo'
Lv_Cadena3= 'según lo que la compañeradijo: " Yo no fui"'
Lv_Cadena4= "El valor del iva es: '0,12'"


print(Lv_Cadena1)
print(Lv_Cadena2)
print(Lv_Cadena3)
print(Lv_Cadena4)

Ln_Valor1=2
Ln_Valor2=2

#suma:

print("suma")
Ln_Result = Ln_Valor1+Ln_Valor2
print(Ln_Result)
print("-------------")

print("resta")
Ln_Result = Ln_Valor1-Ln_Valor2
print(Ln_Result)
print("-------------")

print("multiplicación")
Ln_Result = Ln_Valor1*Ln_Valor2
print(Ln_Result)
print("-------------")

Ln_Result = Ln_Valor1/Ln_Valor2
print(Ln_Result)
print("-------------")

#potencia

print("potencia")
Ln_Result = Ln_Valor1 ** Ln_Valor2
print(Ln_Result)
print("-------------")

#seno
print("seno")
Ln_Result = math.sin(Ln_Valor1) , math.sin(Ln_Valor2)
print(Ln_Result)
print("-------------")

#coseno
print("coseno")
Ln_Result = math.cos(Ln_Valor1) , math.cos(Ln_Valor2)

print(Ln_Result)
print("-------------")

# asignación  

Lv_Variable= 2.3,

print(type(Lv_Variable))
print("-------------")


#caracteres


Lv_frase = "Anita lava la tina"

print ("total de caracteres",  {len(Lv_frase)})
#print(Lv_frase)