import os
import producto
if __name__ == "__main__":
    os.system("cls")
    proveedores = {}
    pro = True
    while pro: 
        os.system("cls")
        print("1.CLIENTE\n2.ADMINISTRADOR\nSeleccione una opcion: ")
        op = int(input(":)"))
        if(op == 1):
            os.system("cls")
            print('+','-'*76,'+')
            print("|{:^30}{:^20}{:^28}|".format(" ","Lista de productos "," "))
            print('+','-'*76,'+')
            print("|{:^15}|{:^15}|{:^15}|{:^15}|{:^14}|".format('Codigo','Nombre','Estado','Precio','Proveedor'))
            if(len(proveedores) >= 1):
                for key,value in proveedores.items():
                    for j,k in value.items():
                        print('+','-'*76,'+')
                        print("|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(k["codigo"],k["nombre"],k["estado"],k["precio"],key))
                        print('+','-'*76,'+')
                print("Presione enter para continuar...")
                input()
            else:
                print("No hay productos registrados\n")
                print("Presione enter para continuar...")
                input()
        if(op == 2):
            os.system("cls")
            print("1.Agregar proveedores: ")
            print("2.Agregar productos: ")
            op= int(input("Selecciona una opcion: "))
            if(op == 1):
                producto.addProveedor(proveedores)
            elif(op == 2):
                producto.addProduct(proveedores)
        
        pro = input("¿Desea Continuar En el programa? S(Si) Enter(No)")

