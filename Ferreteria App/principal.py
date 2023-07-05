import clientes
import productos
import ventas
import compras
import proveedores

if __name__ == "__main__":
    dataClientes={'data':[]}
    dataProductos={'data':[]}
    dataProveedores={'data':[]}
    dataCompras={'data':[]}
    dataVentas={'data':[]}
    diCli = {
        "code":"002",
        "name":"Pepito Perez"
    }
    print(clientes.createData())
    clientes.createData("clientes.json",dataClientes,diCli)
    # productos.createData("productos.json",dataProductos)
    # proveedores.createData("proveedores.json",dataProveedores)
    # compras.createData("compras.json",dataCompras)
    # ventas.createData("ventas.json",dataVentas)
    