mail = input("Ingrese una dirección de correo electrónico: ")
cantidad = 0
x = 0


while x < len(mail):
    if mail[x] == "@":
        cantidad = cantidad + 1
    x = x + 1


if cantidad == 1:
    print("Contiene un solo caracter @ el mail ingresado")
else:
    print("Incorrecto")
