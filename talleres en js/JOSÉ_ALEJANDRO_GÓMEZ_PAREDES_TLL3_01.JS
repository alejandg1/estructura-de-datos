Ln_valor = 4;
Ln_result = Ln_valor % 2;

if (Ln_result == 0) {
  console.log("El número es par");
} else {
  console.log("El número es impar");
}

console.log("-------------------------------------------");

Ln_valor = 4;

if (Ln_result > 0) {
  console.log("El número es positivo");
} else {
  console.log("El número es negativo");
}

console.log("-------------------------------------------");
if (Ln_result == 0) {
  if (Ln_result > 0) {
    console.log("El número es par positivo");
  } else {
    console.log("El número es par negativo");
  }
} else {
  if (Ln_result > 0) {
    console.log("El número es impar positivo");
  } else {
    console.log("El número es impar negativo");
  }
}
