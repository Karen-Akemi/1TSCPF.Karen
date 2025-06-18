#Usando WHILE

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

p = 0
i = 0

ini = min(n1, n2) + 1
f = max(n1, n2)

while ini < f:
    if ini % 2 == 0:
        p += 1
    else:
        i += 1
    ini += 1
print(f"Entre {n1} e {n2} há {p} números pares e {i} números impares")