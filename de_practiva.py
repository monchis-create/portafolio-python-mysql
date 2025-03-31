class Pedido:
    def __init__(self, cliente, servicio, precio):
        self.cliente = cliente
        self.servicio = servicio
        self.precio = precio

    def __str__(self):
        return f"Cliente: {self.cliente} - Servicio: {self.servicio} - Precio: ${self.precio:.2f}"

class Negocio:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, cliente, servicio, precio):
        pedido = Pedido(cliente, servicio, precio)
        self.pedidos.append(pedido)

    def procesar_pedidos(self):
        while self.pedidos:
            yield self.pedidos.pop(0)  # Retorna y elimina el primer pedido en la lista

# Crear una instancia del negocio
mi_negocio = Negocio()

# Agregar pedidos
mi_negocio.agregar_pedido("Juan", "Copia de llave", 1.00)
mi_negocio.agregar_pedido("María", "Cambio de cuadro de licuadora", 7.50)
mi_negocio.agregar_pedido("Carlos", "Cambio de carbones", 6.50)
mi_negocio.agregar_pedido("Ana", "Cambio de manguera de licuadora", 3.50)

# Procesar pedidos uno por uno
procesador = mi_negocio.procesar_pedidos()
for pedido in procesador:
    print("Procesando:", pedido) 