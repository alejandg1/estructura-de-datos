const fs = require("fs");
const path = require("path");

const Fl_Ruta_File = path.join(
  "C:",
  "Users",
  "UNEMI",
  "Pictures",
  "Nueva carpeta",
  "Arcivo190523_01.txt"
);

const Lf_Ruta_Absoluta = path.resolve(Fl_Ruta_File);
console.log(Lf_Ruta_Absoluta);

const Lb_Existe = fs.existsSync(Fl_Ruta_File);
console.log("¿La ruta existe?::  ", Lb_Existe);

const Lf_nombre_file = path.basename(Fl_Ruta_File);
console.log("nombre del archivo: ", Lf_nombre_file);

console.log("+++++");

const Lf_Ruta_raiz = path.dirname(Fl_Ruta_File);
console.log("El nombre del directorio raiz es: ", Lf_Ruta_raiz);
