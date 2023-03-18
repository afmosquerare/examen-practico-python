numeros = []
multiplosDe2 = 0
multiplosDe3 = 0
multiplosDe2Y3 = 0

for i in range(20):
    numero = int(input("Ingresa un número entero: "))
    numeros.append(numero)
    
for numero in numeros:
    if numero % 2 == 0:
        multiplosDe2 += 1
    if numero % 3 == 0:
        multiplosDe3 += 1
    if numero % 2 == 0 and numero % 3 == 0:
        multiplosDe2Y3 += 1

print("Números ingresados que son múltiplos de 2: ", multiplosDe2)
print("Números ingresados que son múltiplos de 3: ", multiplosDe3)
print("Números ingresados que son múltiplos de 2 y 3: ", multiplosDe2Y3)