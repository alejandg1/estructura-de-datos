const path = require("path");
const fs = require("fs");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const Fl_Ruta_File = "/home/alejandro/workspace/dev/Archivo190523_05.txt";
const Lb_existe_root = fs.existsSync(path.dirname(Fl_Ruta_File));
try {
  console.log("Verificando archivo...");
  if (Lb_existe_root) {
    const Lb_existe_File = fs.existsSync(Fl_Ruta_File);
    if (Lb_existe_File) {
      fs.readFile(Fl_Ruta_File, "utf8", (err, data) => {
        if (err) throw err;
        console.log(data);
        console.log("fin del archivo existente");
      });
    } else {
      readline.question(
        "El archivo no existe, ¿Desea crearlo? ",
        (lv_opcion) => {
          if (lv_opcion === "s" || lv_opcion === "S") {
            fs.writeFile(
              Fl_Ruta_File,
              "Esta es mi primera linea del 6to archivo" +
                "Esta es mi tercera linea del 6to archivo\n" +
                "Esta es mi tercera linea del 6to archivo con salto de linea\n",
              (err) => {
                if (err) throw err;
                console.log("su 6to archivo ha sido creado");
              }
            );
          } else if (lv_opcion === "n" || lv_opcion === "N") {
            console.log("Proceso terminado");
          } else {
            console.log("opcion invalida");
          }
          readline.close();
        }
      );
    }
  } else {
    console.log("La ruta especifica no existe, contacte al area de sistemas");
  }
} catch (err) {
  console.log("No se puede crear el File: ", err);
}
