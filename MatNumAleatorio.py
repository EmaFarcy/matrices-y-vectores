# Intresar por teclado la cantidad de filas y columnas de una matriz
# y luego cargarla de números aleatorios cuyo rango lo ingresa el usuario. Calcular el mayor de la primera columna
import random
N=0
Mat=[]
F=0
C=0
Min=0
Max=0
Msj=""
Mayor=0

print("Ingresar filas")
F=int(input(""))
print("Ingresar columnas")
C=int(input(""))

for i in range (0, F):
    Mat.append([0]*C)

print("Ingrese menor rango")
Min=int(input(""))
print("Ingrese mayor rango")
Max=int(input(""))

for i in range (0, F):
    for j in range (0, C):
        N=random.randint(Min, Max)
        Mat[i][j]=N
        Msj=Msj + "" + str(N)
    Msj="\n"
print(Msj)

for i in range (0, F):
    for j in range (0, C):
        if (F==0 and C==0):
            Mayor= Mat[i][j]
        if (j==0):
            if(Mat[i][j]>Mayor):
                Mayor=Mat[i][j]
Msj=str(Mayor) + " es el mayor de la primera columna"
print(Msj)
