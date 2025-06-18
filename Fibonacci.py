#Usando WHILE

nro = int(input("Digite um número: "))


a = 0
b = 1



if nro == 1:
    print(a)
elif nro == 2:
    print(a)
    print(b)
elif nro == 0:
    print("Digite um número acima zero")
else:
    print(a)
    print(b)
    total = a + b
    print(total)
    while total <= nro:
        a = b
        b = total
        total = a + b
        print(total)