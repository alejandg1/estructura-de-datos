const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function leerValor() {
  rl.question(
    "Introduce un valor, para acabar la ejecución ingrese el 0: ",
    (valor) => {
      if (parseFloat(valor) !== 0) {
        console.log("hola");
        leerValor();
      } else {
        console.log("Fin del programa");
        rl.close();
      }
    }
  );
}

leerValor();
