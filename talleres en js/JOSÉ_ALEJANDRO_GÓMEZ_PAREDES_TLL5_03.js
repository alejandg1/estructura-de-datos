const path = require("path");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const fs = require("fs");

const fl_Ruta_File = "/home/alejandro/workspace/dev/Archivo190523_03.txt";
const lb_existe = fs.existsSync(fl_Ruta_File);

if (lb_existe) {
  fs.readFile(fl_Ruta_File, "utf8", (err, data) => {
    if (err) throw err;
    console.log(data);
    console.log("fin del archivo existente");
  });
} else {
  //crea prompt en la terminal
  rl.question("El archino no existe, ¿Desea crearlo? ", (lv_opcion) => {
    if (lv_opcion === "s" || lv_opcion === "S") {
      fs.writeFile(
        fl_Ruta_File,
        "Esta es mi primera linea del 5to archivo" +
          "Esta es mi tercera linea del 5to archivo\n" +
          "Esta es mi tercera linea del 5to archivo con salto de linea\n",
        (err) => {
          if (err) throw err;
          console.log("El archivo ha sido creado!");
        }
      );
    } else if (lv_opcion === "n" || lv_opcion === "N") {
      console.log("Proceso terminado");
    } else {
      console.log("opcion invalidaa");
    }
  });
}
