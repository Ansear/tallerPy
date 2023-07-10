import os
import producto
import proveedor
import compra
if __name__ == "__main__":
    os.system("clear")
    proveedores = {}
    compras  = []
    ventas = []
    pro = True
    while pro: 
        os.system("clear")
        print("1.Agregar proveedores y productos")
        print("2.Comprar productos")
        print("3.Vender productos") 
        print("4.Ver Compras")
        print("5.Ver Ventas")
        op = int(input("Selecciona una opcion "))
        if(op == 1):
            os.system("cls")
            print("1.Agregar Proveedor: ")
            print("2.Agregar Producto: ")
            op = int(input("Selecciona una opcion: "))
            if(op == 1):
                proveedor.addProveedor(proveedores)
            elif(op == 2):
                producto.addProduct(proveedores)
        elif(op == 2):
            compra.showProducts(proveedores)
            if(len(proveedores) >= 1):
                print("Ingrese el nombre del producto a comprar: ")
                nom = input(": ")
                compra.newCompra(nom, proveedores, compras)
        elif(op == 3):
            producto.purchases(proveedores)            
        elif(op == 4):
            print(compras)

        
        op = input("¿Desea Continuar En el programa? S(Si) N(No)")
        op = op.upper()
        if(op == "S"):
            pro = True
        elif(pro == "N"):
            pro = False
        else: 
            pro = False
            print("Error,valor invalido")
            print("Presiona enter para continuar....")
            input()