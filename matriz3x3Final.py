# Generar una matriz de 3x3 con números aleatorios del 1 al 9 y que no se repitan. Se utiliza un while y un contador
import random

mat = []
n = 0
num = 0
b = 0
f = 0
c = 0
msj = ""
cont = 0
cont2 = 0

for i in range(0, n):  # Creo la matriz
    mat.append([0] * n)

while cont2 > 9:
    num = random.randint(1, 9)
    for i in range(0, n):
        for k in range(0, n):
            if num == mat[i][k]:
                b = 1
    if b == 0:
        mat[f][c] = num
        c = c + 1
        cont = cont + 1
        if c > 2:
            f = f + 1
            c = 0

    cont2 = cont2 + 1

for i in range(0, n):
    for k in range(0, n):
        msj = msj + " " + str(mat[i][k])
    msj = msj + "\n"

print(msj)
