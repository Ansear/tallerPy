import os
import producto
if __name__ == "__main__":
    os.system("clear")
    proveedores = {}
    compras  = []
    pro = True
    while pro: 
        os.system("clear")
        print("1.CLIENTE\n2.ADMINISTRADOR\nSeleccione una opcion: ")
        op = int(input(":)"))
        if(op == 1):
            os.system("clear")
            print("1.Ver productos") 
            producto.showProducts(proveedores)
            print("Presione enter para continuar...")
            input()
        elif(op == 2):
            os.system("clear")
            print("1.Agregar proveedores: ")
            print("2.Agregar productos: ")
            print("3.Ver Compras: ")
            op= int(input("Selecciona una opcion: "))
            if(op == 1):
                producto.addProveedor(proveedores)
            elif(op == 2):
                producto.addProduct(proveedores,compras)
            elif(op == 3):
                print(compras)
        
        pro = input("¿Desea Continuar En el programa? S(Si) Enter(No)")

