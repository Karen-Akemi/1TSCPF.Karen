titulo = "Tabuada"
print(f'{titulo:^30}')

nro = int(input("Entre com o valor da tabuada: "))
i = 1

while i <= 100:
    if nro % 2 == 0:
        tabuada = nro * i
        print(nro, "X", i, "=", tabuada)
        i += 2
    elif nro % 2 == 1:
        tabuada = nro * i
        print(nro, "X", i, "=", tabuada)
        i += 3
