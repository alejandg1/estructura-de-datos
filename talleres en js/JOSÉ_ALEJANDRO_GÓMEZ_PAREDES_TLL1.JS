Lv_cadena1 = "Hola mundo";
Lv_cadena2 = "hola mundo";
Lv_cadena3 = 'segpun lo que la compañera dijo: "yo no fuí"';
Lv_cadena4 = "El valor del iva es: '0,12'";

console.log("---------------------------");
console.log(Lv_cadena1);
console.log(Lv_cadena2);
console.log(Lv_cadena3);
console.log(Lv_cadena4);

console.log("---------------------------");
Ln_valor1 = 4;
Ln_valor2 = 2;

console.log("suma: ", Ln_valor1, " + ", Ln_valor2);
Ln_result = Ln_valor1 + Ln_valor2;
console.log(Ln_result);
console.log("---------------------------");

console.log("resta: ", Ln_valor1, " - ", Ln_valor2);
Ln_result = Ln_valor1 - Ln_valor2;
console.log(Ln_result);
console.log("---------------------------");

console.log("multiplicación: ", Ln_valor1, " * ", Ln_valor2);
Ln_result = Ln_valor1 * Ln_valor2;
console.log(Ln_result);
console.log("---------------------------");

console.log("potencia");

console.log("base: ", Ln_valor1, "exponente: ", Ln_valor2);
Ln_result = Ln_valor1 ** Ln_valor2;
console.log(Ln_result);
console.log("---------------------------");

console.log("seno");
console.log("número :", Ln_valor1);

(Ln_result = Math.sin(Ln_valor1)), console.log(Ln_result);
console.log("Número: ", Ln_valor2);

Ln_result = Math.sin(Ln_valor2);

console.log(Ln_result);
console.log("---------------------------");
console.log("coseno");
console.log("número :", Ln_valor1);

(Ln_result = Math.cos(Ln_valor1)), console.log(Ln_result);
console.log("Número: ", Ln_valor2);

Ln_result = Math.cos(Ln_valor2);

console.log(Ln_result);
console.log("---------------------------");

(Lv_variable = 2.3), console.log(typeof Lv_variable);
console.log("------------------");

//caracteres

Lv_frase = "Anita lava la tina";

console.log("total de caracteres: ", Lv_frase.length);
