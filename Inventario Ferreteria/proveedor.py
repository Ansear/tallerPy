import os

def addProveedor(proveedores: list):
    addProveedor =  True
    while addProveedor:
        os.system("cls")
        provee = input("Ingrese el nombre del proveedor: ")
        provee = provee.upper()
        proveedor = {
            provee:{},
        }
        proveedores.update(proveedor)
        op = input("¿Desea Agregar otro proveedor? S(si) N(No): ")
        op = op.upper()
        if(op == "S"):
            addProveedor = True
        elif(op == "N"):
            addProveedor = False
            os.system("cls")
        else: 
            addProveedor = False
            print("Error,valor invalido")
            print("Presiona enter para continuar....")
            input()