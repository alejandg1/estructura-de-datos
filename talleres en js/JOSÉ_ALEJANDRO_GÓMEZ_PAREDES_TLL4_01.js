// crear archivo txt

const fs = require("fs");

fs.appendFileSync(
  "Archivo170523_01.txt",
  "Esta es la primera linea de mi primer archivo"
);
fs.appendFileSync(
  "Archivo170523_01.txt",
  "Esta es la segunda linea de mi primer archivo\n"
);
fs.appendFileSync(
  "Archivo170523_01.txt",
  "Esta es la tercera linea de mi primer archivo con salto de linea"
);
console.log("Su primer archivo ha sido creado, felicidades");
