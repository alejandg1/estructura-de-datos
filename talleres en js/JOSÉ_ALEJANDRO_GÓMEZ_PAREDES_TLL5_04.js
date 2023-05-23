const path = require("path");
const fs = require("fs");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const fl_Ruta_File = "/home/alejandro/workspace/dev/Archivo190523_04.txt";
const lb_existe_root = fs.existsSync(path.dirname(fl_Ruta_File));
if (lb_existe_root) {
  const lb_existe_File = fs.existsSync(fl_Ruta_File);
  if (lb_existe_File) {
    fs.readFile(fl_Ruta_File, "utf8", (err, data) => {
      if (err) throw err;
      console.log(data);
      console.log("fin del archivo existente");
    });
  } else {
    readline.question("El archivo no existe, ¿Desea crearlo? ", (lv_opcion) => {
      if (lv_opcion.toLowerCase() === "s") {
        fs.writeFile(
          fl_Ruta_File,
          "Esta es mi primera linea del 6to archivo\n" +
            "Esta es mi segunda linea del 6to archivo\n" +
            "Esta es mi tercera linea del 6to archivo con salto de linea\n",
          (err) => {
            if (err) throw err;
            console.log("su 6to archivo ha sido creado");
          }
        );
      } else if (lv_opcion.toLowerCase() === "n") {
        console.log("Proceso terminado");
      } else {
        console.log("opcion invalida");
      }
      readline.close();
    });
  }
} else {
  console.log("La ruta especifica no existe, contacte al area de sistemas");
}
