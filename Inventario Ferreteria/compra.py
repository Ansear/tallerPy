import os

def compra(proveedores):
    print("Ingrese la cantidad de produtos a comprar: ")                
    pro = int(input("Ingrese el producto que necesita comprar: "))
    cant = int(input("ingrese la cantidad de produtos a comprar: "))
    fecha = input("Ingrese la fecha (DD/MM/AAAA):")
    while addProduct:
        os.system("clear")        
        op = input("¿Desea agregar un producto? S(Si) N(No): ")
        if(op == "S"):
            os.system("clear")
            nombre = input("Ingrese el nombre del producto: ")
            precio = int(input(f"Ingrese el precio del producto: {nombre} c/u: "))
            stockMinimo = input("Ingrese el stock minimo del producto: ")
            stockMaximo = int(input("Ingrese el stock maximo del producto: "))
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
            nomPro = name
            numCompra += 1
            os.system("clear")
            fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
            valCompra = stockMaximo * precio
            
            numCompra = {
                "proveedor":name,
                "producto":nombre,
                "Numero Compra":numCompra,
                "Fecha Compra":fecha,
                "Valor Compra":valCompra,
                "Cantidad Comprada":stockMaximo
            }
            compras.append(numCompra)            

            op = bool(input("¿Desea agregar otro producto? 1.(Si) 2(No)"))
            if(op == 1):
                addProducto = True
            elif(op == 2):
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
        numCompra = {
            "proveedor":name,
            "producto":nombre,
            "Numero Compra":numCompra,
            "Fecha Compra":fecha,
            "Valor Compra":valCompra,
            "Cantidad Comprada":stockMaximo
        }
        compras.append(numCompra)   

def showProducts(proveedores):
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
    else:
            print("No hay productos registrados\n")
            print("Presione enter para continuar...")
            input()