# Programar una agenda con matrices
op = 0
i = 1
b = 0
mat = []
mat.append([""] * 4)
mat[0][0] = "Dni "
mat[0][1] = "Nombre "
mat[0][2] = "Apellido "
mat[0][3] = "Teléfono "
fin = False

while fin == False:
    msj = "1 Agregar, 2 Buscar, 3 Imprimir, 4 Salir: "
    op = int(input(msj))
    if op == 1:
        dni = input("Ingresar DNI: ")
        nom = input("Ingresar nombre: ")
        ape = input("Ingresar apellido: ")
        tel = input("Ingresar teléfono: ")
        mat.append([""] * 4)
        mat[i][0] = dni
        mat[i][1] = nom
        mat[i][2] = ape
        mat[i][3] = tel
        i = i + 1
    if op == 4:
        fin = True
    if op == 2:
        dni = input("Ingresar DNI: ")
        for f in range(0, i):
            for c in range(0, 4):
                if dni == mat[f][c]:
                    b = 1
                    nom = mat[f][1]
                    ape = mat[f][2]
                    tel = mat[f][3]
                    msj = dni + " " + nom + " " + ape
                    print(msj)
        if b == 0:
            print("Cliente inexistente")
