import os

con = 0
msj = ""
mat = []
mat2 = []
fin = False

for i in range(0, 10):
    mat.append([0] * 10)
    mat2.append(["-"] * 10)

mat[0][0] = 1
mat[0][1] = 1
mat[0][2] = 1
mat[0][3] = 1

mat[3][0] = 1
mat[3][1] = 1
mat[3][2] = 1

mat[8][2] = 1
mat[8][3] = 1
mat[8][4] = 1

while fin == False:
    f = int(input("Ingresar fila: "))
    c = int(input("Ingreasr columna: "))
    os.system("cls")
    if mat[f][c] == 1:
        if mat2[f][c] == "-":
            mat2[f][c] = "x"
            con = con + 1
    else:
        mat2[f][c] = "0"

    for i in range(0, 10):
        for k in range(0, 10):
            msj = msj + "" + mat2[i][k]
        msj = msj + "\n"
    print(msj)
    if con == 10:
        fin = True
    msj = ""
