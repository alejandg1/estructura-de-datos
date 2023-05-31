# proceso de encriptación de clave
Alfabeto= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
clave="!#$%&/()=?¿¡'1234567890@|~€¬`+ç-.,;:_Ç^*<ªº>ñÑQwesdgxp"

Lv_frase = "Anita lava la tina"


def Pcr_Enciptado(Lv_frase):
    Ov_Frase_escriptada =""
    for letra in Lv_frase:
        if(letra in Alfabeto):
           indice= Alfabeto.index(letra)
           Letra_encriptada=clave[indice]
           Ov_Frase_escriptada+=Letra_encriptada

        else:
            Ov_Frase_escriptada+=letra
    return Ov_Frase_escriptada

def Pcr_desenciptado(Lv_frase_encriptada):
    Ov_Frase_desescriptada =""
    for letra in Lv_frase_encriptada:
        if(letra in clave):
           indice= clave.index(letra)
           Letra_desencriptada=Alfabeto[indice]
           Ov_Frase_desescriptada+=Letra_desencriptada

        else:
            Ov_Frase_desescriptada+=letra
    return Ov_Frase_desescriptada



Lv_frase_encriptada=Pcr_Enciptado(Lv_frase)

##ENCRIPTAR
print(f"la frase encriptada es: {Lv_frase_encriptada}")
##DESENCRIPTAR
Lv_frase_desencriptada = Pcr_desenciptado(Lv_frase_encriptada)
print(f"la frase encriptada es: {Lv_frase_desencriptada}")
 

