let Ln_Valor = 6;
let Ln_Result = Ln_Valor % 2;
console.log("--------------------------------------------------------");
console.log("presentar por pantalla si es par o no");
console.log(`El número ${Ln_Valor} es par?: `);
if (Ln_Result == 0) {
  console.log("si es par");
} else {
  console.log("no es par");
}
console.log("--------------------------------------------------------");

console.log("Recuperando el valor de un número entero");
Ln_Valor = 28.129;
let Ln_Parte_Entera = Math.floor(Ln_Valor);
console.log(Ln_Parte_Entera);
console.log("");

console.log("Recuperando la parte entera en una variable int");
Ln_Parte_Entera = parseInt(Ln_Valor);
console.log(Ln_Parte_Entera);
console.log("");

console.log("Recuperando la parte decimal");
let Ln_Parte_Decimal = Ln_Valor - Math.floor(Ln_Valor);
console.log(Ln_Parte_Decimal);
console.log("");

console.log("Redondeo");
Ln_Parte_Decimal = Math.round((Ln_Valor - Math.floor(Ln_Valor)) * 100) / 100;
console.log(Ln_Parte_Decimal);
console.log("");
console.log("Truncar con Math.trunc");
Ln_Parte_Decimal = Math.trunc(Ln_Valor);
console.log(Ln_Parte_Decimal);
console.log("");

console.log("Truncar con Math.floor");
Ln_Valor = 80.1265;
Ln_Parte_Entera = Math.floor(Ln_Valor);
Ln_Parte_Decimal = Ln_Valor - Ln_Parte_Entera;
console.log(Ln_Parte_Decimal.toFixed(4));
console.log("");
