"""Cargar 2 matrices de (2x3) numeros aleatorios (1 al 9) y calcular: a) producto escalar b)Imprimir las dos matrices con la expresion"""
import random
mat1 = []
mat2 = []
filas = 2
col = 3
msj = ""
prodEscalar = 0
resultado = 0 
con = 0
#CREAR DOS MATRICES
for i in range(0, filas): 
    mat1.append([0]*col)
    mat2.append([0]*col)
#CARGAR MATRIZ 1
for i in range(0, filas):
    for j in range(0, col):
        numero = random.randint(1, 9)
        mat1[i][j]=numero
#CARGAR MATRIZ 2
for i in range(0, filas):
    for j in range(0, col):
        numero = random.randint(1, 9)
        mat2[i][j]=numero
#IMPRIMIR MATRIZ 1
for i in range(0, filas):
    for j in range(0, col):
        L = len(str(mat1[i][j]))
        if(L ==1):
            msj = msj + "  " + str(mat1[i][j])
        if(L == 2):
            msj = msj + " " + str(mat1[i][j])
    msj = msj + "\n" 
print(msj)
msj = "" #limpiar msj para q no se pise
#IMPRIMIR MATRIZ 2
for i in range(0, filas):
    for j in range(0, col):
        L = len(str(mat2[i][j]))
        if(L ==1):
            msj = msj + "  " + str(mat2[i][j])
        if(L == 2):
            msj = msj + " " + str(mat2[i][j])
    msj = msj + "\n" 
print(msj)
msj = ""
#PRODUCTO ESCALAR (ej. el 0,0 de mat1 se multiplica con el 0,0 de mat2, el 0,1 de mat1 con el 0,1 de mat2 ...)
for i in range(0, filas):
    for j in range(0, col):
       prodEscalar = mat1[i][j] * mat2[i][j]
       resultado = resultado + prodEscalar
msj = ""
#IMPRIMIR
for i in range(0, filas):
    for j in range(0, col):
            if(con < 5):
                msj = msj + str(mat1[i][j]) + " x " + str(mat2[i][j]) + " + " #msj = msj para que imprima uno al lado del otro
            else:
                msj = msj + str(mat1[i][j]) + " x " + str(mat2[i][j])
            con = con + 1
msj = msj + " = " + str(resultado)
print(msj)

