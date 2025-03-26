# CODIGO SUPER RECONTRA MEJORADO



from tabulate import tabulate

# 📌 1️⃣ Clase para gestionar pedidos
class Pedido:
    pedidos = []

    @classmethod
    def agregar_pedido(cls, id_pedido, cliente, servicio, precio, estado="pendiente"):
        cls.pedidos.append({
            "ID": id_pedido, "Cliente": cliente, "Servicio": servicio,
            "Precio": precio, "Estado": estado
        })

    @classmethod
    def mostrar_pedidos(cls):
        print("\n📋 Lista de Pedidos:")
        print(tabulate(cls.pedidos, headers="keys", tablefmt="fancy_grid"))

    @classmethod
    def actualizar_estado(cls, id_pedido, nuevo_estado):
        for pedido in cls.pedidos:
            if pedido["ID"] == id_pedido:
                pedido["Estado"] = nuevo_estado
                print(f"✅ Pedido {id_pedido} actualizado a '{nuevo_estado}'")
                return
        print(f"⚠️ Pedido {id_pedido} no encontrado.")

# Agregamos pedidos
Pedido.agregar_pedido(1, "Juan Pérez", "Copia de llave", 1.00)
Pedido.agregar_pedido(2, "María López", "Cambio de cuadro de licuadora", 7.50, "completado")
Pedido.agregar_pedido(3, "Carlos Díaz", "Reparación de olla de presión", 10.00)
Pedido.agregar_pedido(4, "Ana Torres", "Cambio de carbones", 6.50)

Pedido.mostrar_pedidos()
Pedido.actualizar_estado(3, "completado")
Pedido.mostrar_pedidos()


# 📌 2️⃣ Clase para gestionar inventario
class Inventario:
    productos = {
        "M1": {"Nombre": "Cuchillas de licuadora", "Cantidad": 15, "Precio": 9.00},
        "M2": {"Nombre": "Carbones de motor", "Cantidad": 30, "Precio": 4.50},
        "M3": {"Nombre": "Empaques de olla de presión", "Cantidad": 20, "Precio": 6.00}
    }

    @classmethod
    def mostrar_inventario(cls):
        print("\n📦 Inventario:")
        data = [{"Código": k, **v} for k, v in cls.productos.items()]
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

    @classmethod
    def actualizar_stock(cls, codigo, cantidad_vendida):
        if codigo in cls.productos:
            if cls.productos[codigo]["Cantidad"] >= cantidad_vendida:
                cls.productos[codigo]["Cantidad"] -= cantidad_vendida
                print(f"✅ Stock actualizado: {cls.productos[codigo]['Nombre']} → {cls.productos[codigo]['Cantidad']} unidades restantes.")
            else:
                print(f"⚠️ No hay suficiente stock de {cls.productos[codigo]['Nombre']}.")
        else:
            print("⚠️ Producto no encontrado.")

Inventario.mostrar_inventario()
Inventario.actualizar_stock("M2", 4)
Inventario.mostrar_inventario()


# 📌 3️⃣ Tarifas como tuplas inmutables
SERVICIOS = (
    ("Copia de llave", 1.00),
    ("Cambio de cuadro de licuadora", 7.50),
    ("Cambio de carbones", 6.50),
    ("Reparación de olla de presión", 10.00)
)

def mostrar_tarifas():
    print("\n💰 Tarifas de Servicios:")
    print(tabulate(SERVICIOS, headers=["Servicio", "Precio ($)"], tablefmt="fancy_grid"))

mostrar_tarifas()