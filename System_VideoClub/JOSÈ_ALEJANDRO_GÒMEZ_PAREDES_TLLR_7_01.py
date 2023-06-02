from cryptography.fernet import Fernet

clave = Fernet.generate_key()

## crear objeto fernet con la clave generada
fernet = Fernet(clave)


texto_original = "Anita lava la tina"


## cifrar el texto
texto_cifrado=fernet.encrypt(texto_original.encode())

## descifrar el texto
texto_descifrado=fernet.encrypt(texto_cifrado).decode()
print("-----------------------------------")
print(("Texto Original",texto_original))
print("-----------------------------------")
print(("Texto cifrado",texto_cifrado))
print("-----------------------------------")
print(("Texto descifrado",texto_descifrado))