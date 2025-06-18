titulo = "Tabuada"
print(f'{titulo:^30}')

nro = int(input("Entre com o valor da tabuada: "))

for i in range(1, 11):
    tabuada = nro * i
    print(nro, "X", i, "=", tabuada)

