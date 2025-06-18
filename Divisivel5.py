#Usando FOR
titulo = "Divisível por 5"
print(f'{titulo:^30}')

i = int(input("Digite o primeiro número: "))
f = int(input("Digite o segundo número: "))

for nro in range(i, f):
    if nro % 5 == 0:
        print(nro)

for nro in range(f, i):
    if nro % 5 == 0:
        print(nro)