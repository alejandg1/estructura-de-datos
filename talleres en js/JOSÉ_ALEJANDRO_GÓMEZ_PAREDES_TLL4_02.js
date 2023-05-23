const fs = require("fs");
fs.writeFile(
  "Archivo170523_02.txt",
  "Esta es la primera liena de mi primer archivoEsta es la segunda liena de mi primer archivo\nEsta es la tercera liena de mi primer archivo con salto de linea",
  //manrjar algun error posible
  (err) => {
    if (err) throw err;
    console.log("su segundo archivo ha sido creado, vamos bien.");
  }
);
