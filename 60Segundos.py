import time
#Usando FOR
titulo = "60 segundos"
print(f'{titulo:^30}')

for s in range(60, 0, -1):
    time.sleep(1)
    print(s)