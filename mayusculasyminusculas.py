texto = input("Ingresa un texto: ")
cantidad1 = 0
cantidad2 = 0  
x = 0

while x < len(texto):
    if texto[x].islower():  
        cantidad1 += 1
    elif texto[x].isupper():  
        cantidad2 += 1
    x += 1  


print("Cantidad de mayúsculas:", cantidad2)
print("Cantidad de minúsculas:", cantidad1)
