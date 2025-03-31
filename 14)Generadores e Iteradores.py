# ejemplo de iterador

# Crear una lista.
my_list = [1, 2, 3, 4]

# Obtener el iterador.

my_iter = iter(my_list)

# Usar el iterador.
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
# print(next(my_iter))  # Error: StopIteration


# ----------------------------------------------------------------------------------------------------

# Iterar en cadenas
# Creando una cadena.
text = "Hola Mundo"

# Crear un iterador.
iter_text = iter(text)

# Iterar en la cadena.
for char in iter_text:
    print(char)

# ----------------------------------------------------------------------------------------------------

# Crear un iterador para los numeros impares.

# Limite
limit = 10 

# Crear un iterador.
odd_itter = iter(range(1, limit+1, 2))

#Usar el iterador.
for num in odd_itter:
    print(num)

# ----------------------------------------------------------------------------------------------------

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
# ----------------------------------------------------------------------------------------------------

# fibonacci
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
# ----------------------------------------------------------------------------------------------------

# Codigo mejorado



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