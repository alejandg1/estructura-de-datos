console.log("------------longitud de la frase original----------")
Lv_frase="Anita lava la tina"

console.log(Lv_frase);

console.log("-----------------------frase quemada--------------------------");

Lv_frase="Anita"+"-"+"lava"+"-"+"la"+"-"+"tina"


console.log("cadena de caracteres modificada manualmente (quemada: )", Lv_frase)

Lv_frase="Anita"


console.log("--------------------frase repetida por multiplicación---------------------");



console.log("opción 1: "+ Lv_frase.repeat(5));

Lv_frase = Lv_frase+" "
console.log("opción 2: "+  Lv_frase.repeat(5));

console.log("opción 3: "+(Lv_frase+"").repeat(5));

Lv_frase= "Anita "
console.log("opción 4: "+Lv_frase.repeat(5));

Lv_frase+=" "
console.log("opción 5: "+Lv_frase.repeat(5));


console.log(" -----------------hallar caracter o conjunto de caracteres en un str---------------------");

Lv_frase = "Anita lava la tina"

Lv_frase_Encontrar =Lv_frase.indexOf("tina") 
console.log(Lv_frase_Encontrar);
Lv_frase_Encontrar =Lv_frase.indexOf("Tina") 
console.log(Lv_frase_Encontrar);



console.log("----------------------frase en mayuscula y minuscula--------------------");

console.log(Lv_frase.toLowerCase());
console.log(Lv_frase.toUpperCase());

console.log("----------------------que la primera letra sea mayuscula---------------------");
console.log("javascript no posee función propia para esto");

console.log("-----------reemplazar caracteres o conjunto de caracteres de un str----------------------------------------");


console.log("---------------reemplazo manual-------------------");
console.log(Lv_frase.replace("l","a"));

Lv_frase2="nosotros"
console.log("---------------reemplazo por variables-------------------");
console.log(Lv_frase.replace("anita",Lv_frase2));

console.log("-----------------------------eliminando caracteres con .replace()");

console.log(Lv_frase.replace("a",""));

console.log("-------------------------salto de lineas-----------------------");
Lv_frase= "Anita \n lava \n la \n tina"

console.log(Lv_frase);


console.log("---------------------recuperando subcadena -----------------------")
Lv_frase="Anita lava la tina"

Lv_frase2= Lv_frase.substring(6,10)
console.log(Lv_frase2);
Lv_frase2= Lv_frase.substring(14,18)
console.log(Lv_frase2);


Lv_frase2="hola mundo"

console.log("total de caracteres: ", Lv_frase2.length);

console.log("----------------------cadena caracter por caracter--------------------");

console.log(Lv_frase2[0])
console.log(Lv_frase2[1])
console.log(Lv_frase2[2])
console.log(Lv_frase2[3])
console.log(Lv_frase2[4])
console.log(Lv_frase2[5])
console.log(Lv_frase2[6])
console.log(Lv_frase2[7])
console.log(Lv_frase2[8])
console.log(Lv_frase2[9])


console.log("----------------------cadena caracter por caracter en  orden inverso--------------------");


console.log(Lv_frase2[-1])
console.log(Lv_frase2[-2])
console.log(Lv_frase2[-3])
console.log(Lv_frase2[-4])
console.log(Lv_frase2[-5])
console.log(Lv_frase2[-6])
console.log(Lv_frase2[-7])
console.log(Lv_frase2[-8])
console.log(Lv_frase2[-9])
console.log(Lv_frase2[-10])
console.log("javascipt no permite indices negativos")

console.log("-----------------------saltar caracteres-------------------");
console.log(Lv_frase.substring(1,9,2));
console.log(Lv_frase.substring(1,8,4));
console.log(Lv_frase.substring(1,9,3));

console.log("funciona diferente en javascript")