from datetime import date
import os

def addProduct(proveedores: dict):
    addProduct = True
    numCompra = 0
    cont = 1
    while addProduct:
        os.system("cls")        
        print(proveedores)
        op = input("¿Desea agregar un producto? S(Si) N(No): ")
        op = op.upper()
        if(op == "S"):
            os.system("cls")
            nombre = input("Ingrese el nombre del producto: ")
            print(f"Proveedores de {nombre}:")
            if(len(proveedores)>=1):
                
                for k,v in enumerate(proveedores):
                    print(v)
                    
            else:
                print("No hay proveedores registrados")
            namePro = input("Nombre de proveedor: ")
            precio = int(input(f"Ingrese el precio del producto: {nombre} c/u: "))
            cant = input("Ingrese la cantidad del producto: ")
            date = input("Ingrese la fecha(AAAA/MM/DD):")
            cont+=1
            producto = {
                    "codigo": cont,
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cant,
            }
            
            proveedores[namePro.upper()][nombre] = producto
            
            op = (input("¿Desea agregar otro producto? S(Si) N(No)"))
            op = op.upper()
            if(op == "S"):
                addProducto = True
            elif(op == "N"):
                addProducto = False
            else:
                print("Ingrese un dato valido")
                print("Presiona enter para continuar....")
                input()
                addProducto = False
        elif(op == "N"):
            addProduct = False
        else:
            addProveedor = False
            print("Error,valor invalido")
            print("Presiona enter para continuar....")
            input()



# {
#     "juan":{
#         "cod":{},
#         "cod":{}
#         }
#     ,
#     "otro":{},
#     "otromas":{}
# }