##Lv varchar _ Ln number _ Lf fechas _ ld decimal


print("------------longitud de la frase original----------")
Lv_Frase = "Anita lava la tina"


print(len(Lv_Frase))


print("-------------frase quemada-----------")
Lv_Frase = "Anita "+"-"+" lava "+"-"+"la "+"-"+" tina"


print("cadena de caracteres modificada manualmente (quemada):", Lv_Frase)
Lv_Frase = "Anita"

print("--------frase repetida por multiplicación----------------")
##opciones para añadir espacios
print("opcion 1: "+Lv_Frase * 5)

Lv_Frase=Lv_Frase+" "
print("opcion 2: "+Lv_Frase * 5)

print("opcion 3: "+(Lv_Frase+" ") * 5)

Lv_Frase="Anita "
print("opcion 4 : "+Lv_Frase * 5)

Lv_Frase+=" "
print("opcion 5: "+Lv_Frase * 5)



print("  -----------------hallar caracter o conjunto de caracteres en un str---------------------  ")


Lv_Frase = "Anita lava la tina"

Lv_Frase_Encontrar=Lv_Frase.find("tina") 

print(Lv_Frase_Encontrar)
Lv_Frase_Encontrar=Lv_Frase.find("Tina") 
print(Lv_Frase_Encontrar)




print("--------frase en mayuscula y minuscula----------------")

print(Lv_Frase.lower())
print(Lv_Frase.upper())

print("que la primera letra sea mayuscula")

Lv_Frase=(Lv_Frase.lower())
print(Lv_Frase.capitalize())


print("-----------reemplazar caracteres o conjunto de caracteres de un str----------------------------------------")

print("-------------reemplazo manual-------------------")
print(Lv_Frase.replace("l","a"))

Lv_Frase2= "nosotros"
print("----------------reemplazo por variables--------------------------------")
print(Lv_Frase.replace("anita",Lv_Frase2))

print("--------eliminando caracteres con .replace()---------------------")

print(Lv_Frase.replace("a",""))

##posiciones en string

print("--------salto de lineas---------------------")
Lv_Frase = "Anita \n lava \nla \ntina"

print(Lv_Frase)


print("--------recuperando subcadena (posiciones) ---------------------")

Lv_Frase2= Lv_Frase[6:10]
print(Lv_Frase2)
Lv_Frase2= Lv_Frase[14:18]
print(Lv_Frase2)


Lv_Frase2="hola mundo"
print("total de caracteres",len(Lv_Frase2))
print("-------------------cadena mostrada caracter por caracter----------------------")
print(Lv_Frase2[0])
print(Lv_Frase2[1])
print(Lv_Frase2[2])
print(Lv_Frase2[3])
print(Lv_Frase2[4])
print(Lv_Frase2[5])
print(Lv_Frase2[6])
print(Lv_Frase2[7])
print(Lv_Frase2[8])
print(Lv_Frase2[9])

print("-------------------cadena invertida----------------------")
print(Lv_Frase2[-1])
print(Lv_Frase2[-2])
print(Lv_Frase2[-3])
print(Lv_Frase2[-4])
print(Lv_Frase2[-5])
print(Lv_Frase2[-6])
print(Lv_Frase2[-7])
print(Lv_Frase2[-8])
print(Lv_Frase2[-9])
print(Lv_Frase2[-10])



print("-------------------saltar caracteres ----------------------")
print(Lv_Frase2[1:9:2])

print(Lv_Frase2[1:8:4])
print(Lv_Frase2[1:9:3])
