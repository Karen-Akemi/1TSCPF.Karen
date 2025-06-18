#Usando FOR

titulo = "Jogo do PIM"
print(f'{titulo:^30}')

for i in range(1, 31):
    if i % 4 == 0:
        print("PLIM")
    else:
        print(i)