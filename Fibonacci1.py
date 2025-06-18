nro = int(input("Entre com o número de termo de Fibonacci: "))

a, b, i = 0, 1, 1

while i <= nro:
    print(a)
    a, b = b, a + b
    i += 1