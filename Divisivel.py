#Usando FOR
d = int(input("Qual número você quer dividir? "))

for nro in range(0, 100):
    if nro % d == 0:
        print(nro)
