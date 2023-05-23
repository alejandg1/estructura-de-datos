const fs = require("fs");
const Fl_Stream =
  "Esta es la primera línea de mi primer archivo\nEsta es la segunda línea de mi primer archivo\nEsta es la tercera línea de mi primer archivo con salto de línea";
const Lv_información = Fl_Stream;
const archivo_disco = fs.createWriteStream("Archivo170523_03.txt");
archivo_disco.write(Lv_información);
console.log("Su tercer archivo ha sido creado, vamos bien!");
