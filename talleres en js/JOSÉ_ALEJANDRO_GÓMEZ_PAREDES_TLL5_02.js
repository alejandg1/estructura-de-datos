const fs = require("fs");

const Fl_Ruta_File = "/home/alejandro/workspace/dev/Archivo190523_02.txt";

let Lv_contenido = "";
Lv_contenido += "Esta es mi primera linea de codigo";
Lv_contenido += "Esta es mi segunda linea de codigo";
Lv_contenido += "Esta es mi tercera linea de codigo \ncon salto de linea \n";

fs.writeFile(Fl_Ruta_File, Lv_contenido, (err) => {
  if (err) throw err;
  console.log("Su cuarto archivo ha sido creado, vamos bien");
});
