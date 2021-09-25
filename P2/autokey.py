
# Cifrado usando atutoclave
def cifrado_autoclave(mensaje, key):
    mensaje_cifrado = ""
    index = 0
    
    while len(key) != len(mensaje):
        key += mensaje[index]
        index += 1
    for index in range(len(mensaje)):
        character = ((ord(mensaje[index]) + ord(key[index])) % 26) + ord('A')
        mensaje_cifrado += chr(character)

    return mensaje_cifrado


# Descifrando usando autoclave
def descifrado_autoclave(mensaje, key):
    mensaje_descifrado = ""
    index = 0
    while len(key) != len(mensaje):
        key += chr(((ord(mensaje[index]) - ord(key[index])) % 26) + ord('A'))
        index += 1
    
    for index in range(len(mensaje)):
        character = ((ord(mensaje[index]) - ord(key[index])) % 26) + ord('A')
        mensaje_descifrado += chr(character)

    return mensaje_descifrado


print("Presiona 1 para cifrar. \nPresiona 2 para descifrar.")
t = input("Ingresa tu elección : ")

if t == "1":
    mensaje = input("Ingresar mensaje a cifrar : ")
    key = input("Ingresar la clave : ")

    mensaje_cifrado = cifrado_autoclave(mensaje, key)
    print("Mensaje cifrado : " + mensaje_cifrado + "\n")

elif t == "2":
    mensaje = input("Ingresar mensaje a descifrar : ")
    key = input("Ingresa la clave : ")

    mensaje_descifrado = descifrado_autoclave(mensaje, key)
    print("Mensaje descifrado : " + mensaje_descifrado + "\n")

else:
    print("Respuesta incorrecta !!!")

