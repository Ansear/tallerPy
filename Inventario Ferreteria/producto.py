import os

def addProveedor(proveedores: dict):
    addProveedor =  True
    while addProveedor:
        os.system("cls")
        op = bool(input("¿Desea Agregar un proveedor? S(si) Enter(No): "))
        if(op):
            os.system("cls")
            provee = input("Ingrese el nombre del proveedor: ")
            provee = provee.upper()
            proveedor = {
                provee:{},
            }
            proveedores.update(proveedor)
        else: 
            addProveedor = False
            print("Presiona enter para continuar....")
            input()

def addProduct(proveedores: dict):
    addProduct = True

    while addProduct:
        os.system("cls")
        name = input("Ingresa el nombre del proveedor: ")
        name = name.upper()
        if name in proveedores:
            op = bool(input("¿Desea agregar un producto? S(Si) Enter(No): "))
            if(op):
                os.system("cls")
                cod = input("Ingrese el cod del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                precio = input("Ingrese el precio del producto: ")
                stockMinimo = input("Ingrese el stock minimo del producto: ")
                stockMaximo = input("Ingrese el stock maximo del producto: ")
                estado = bool(input("Ingrese el estado del producto: D(Disponible) Enter(No Disponible)"))
                if(estado == True):
                    estado = "Disponible"
                else:
                    estado = "No Disponible"
                
                    
                producto = {
                    cod :{
                        "codigo": cod,
                        "nombre": nombre,
                        "precio": precio,
                        "stockMinimo": stockMinimo,
                        "stockMaximo": stockMaximo,
                        "estado":estado,
                    }
                }
                
                proveedores[name].update(producto)
            else:
                addProduct = False
        else: 
            print("El proveedor no se encuentra")
            print("Presiona enter para continuar....")
            input()
            addProduct = False

# {
#     "juan":{
#         "cod":{},
#         "cod":{}
#         }
#     ,
#     "otro":{},
#     "otromas":{}
# }

        
    
