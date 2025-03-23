
# matrices al igual que las listas podemos añadir iformacion , eliminar , incluso modificarla, esto significa que son datos mutables que pueden cambiar.
matrix = [[1,2,3,77],
          [4,5,6,66],
          [7,8,9,99]]
print(matrix) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][3]) #99 
           # F  C




# matrices
matrix1 = [[[1,2],[3,4]],
           [[5,6],[7,8]]]
print(matrix1) #[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(matrix1[1][0][1])#6
print(matrix1[0][1][1])#4
print(matrix1[1][0][0])#5
            # F  C




# Tenemos clases donde no podemos hacer modificaciones estas son las tuplas en python
# tuplas
tuplas = (1,2,3,4,5,6)
print(tuplas)
print(type(tuplas))
print(tuplas[0])
tuplas[0] = "unos" # No podemos modificar una tupla porque es inmutable, lo que significa que no se pueden cambiar sus elementos después de ser creada.
# Las tuplas son inmutables, por lo que cualquier intento de reasignar un valor a un índice de una tupla, como tuplas[0] = "unos", resultará en un error de tipo (TypeError). 
print(tuplas)

#----------------------------------------------------------------------------------------

# Este codigo  no esta bien optimizado.



# 1️⃣ Estructurar Pedidos con Listas Anidadas
# Podemos usar listas de varias dimensiones para gestionar cada pedido de forma organizada:

# Lista de pedidos donde cada pedido tiene: [ID, Cliente, Servicio, Precio, Estado]
pedidos = [
    [1, "Juan Pérez", "Copia de llave", 1.00, "pendiente"],
    [2, "María López", "Cambio de cuadro de licuadora", 7.50, "completado"],
    [3, "Carlos Díaz", "Reparación de olla de presión", 10.00, "pendiente"],
    [4, "Ana Torres", "Cambio de carbones", 6.50, "pendiente"]
]

# Mostrar pedidos en formato avanzado
for pedido in pedidos:
    print(f"ID: {pedido[0]}, Cliente: {pedido[1]}, Servicio: {pedido[2]}, Precio: ${pedido[3]:.2f}, Estado: {pedido[4]}")








# 2️⃣ Usar Matrices para Controlar Inventario
# Podemos usar una matriz para gestionar el stock de piezas de licuadoras y ollas de presión:

# Matriz de inventario: [Código, Nombre, Cantidad Disponible, Precio Unitario]
inventario = [
    ["M1", "Cuchillas de licuadora", 15, 2.50],
    ["M2", "Carbones de motor", 30, 1.20],
    ["M3", "Empaques de olla de presión", 20, 3.00]
]

# Acceder a información específica
print(f"Stock de {inventario[1][1]}: {inventario[1][2]} unidades disponibles.")
print(f"Precio de {inventario[2][1]}: ${inventario[2][3]:.2f} por unidad.")
print(f"Total de unidades en inventario: {sum([producto[2] for producto in inventario])}")






# 📌 Podemos actualizar el inventario dinámicamente:


# En actulizar stock estan las unidades vendidas en este caso 4 unidades.
def actualizar_stock(codigo, cantidad_vendida):
    for item in inventario:
        if item[0] == codigo:
            item[2] -= cantidad_vendida
            print(f"Stock actualizado: {item[1]} → {item[2]} unidades restantes.")
            return
    print("⚠️ Producto no encontrado.")

# Ejemplo: Vendimos 4 carbones de motor
actualizar_stock("M2", 4)





# 3️⃣ Usar Tuplas para Tarifas Inmutables
# Las tarifas de los servicios no deberían cambiar fácilmente, así que podemos usar tuplas:

# Lista de servicios con tarifas fijas (tuplas)
SERVICIOS = (
    ("Copia de llave", 1.00),
    ("Cambio de cuadro de licuadora", 7.50),
    ("Cambio de carbones", 6.50),
    ("Reparación de olla de presión", 10.00)
)

# Acceder a las tarifas de los servicios
for servicio in SERVICIOS:
    print(f"Servicio: {servicio[0]}, Precio: ${servicio[1]:.2f}")



# ---------------------------------------------------------------------------------------






# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 
# CODIGO MEJORADO 

# 📌 1️⃣ Estructurar Pedidos con Diccionarios (más legible y flexible)
pedidos = [
    {"ID": 1, "Cliente": "Juan Pérez", "Servicio": "Copia de llave", "Precio": 1.00, "Estado": "pendiente"},
    {"ID": 2, "Cliente": "María López", "Servicio": "Cambio de cuadro de licuadora", "Precio": 7.50, "Estado": "completado"},
    {"ID": 3, "Cliente": "Carlos Díaz", "Servicio": "Reparación de olla de presión", "Precio": 10.00, "Estado": "pendiente"},
    {"ID": 4, "Cliente": "Ana Torres", "Servicio": "Cambio de carbones", "Precio": 6.50, "Estado": "pendiente"}
]

def mostrar_pedidos():
    print("\n📋 Lista de Pedidos:")
    for pedido in pedidos:
        print(f"ID: {pedido['ID']}, Cliente: {pedido['Cliente']}, Servicio: {pedido['Servicio']}, "
              f"Precio: ${pedido['Precio']:.2f}, Estado: {pedido['Estado']}")

mostrar_pedidos()

# 📌 2️⃣ Usar Diccionarios para Controlar Inventario
inventario = {
    "M1": {"Nombre": "Cuchillas de licuadora", "Cantidad": 15, "Precio": 9.00},
    "M2": {"Nombre": "Carbones de motor", "Cantidad": 30, "Precio": 4.50},
    "M3": {"Nombre": "Empaques de olla de presión", "Cantidad": 20, "Precio": 6.00}
}

def mostrar_inventario():
    print("\n📦 Inventario:")
    for codigo, datos in inventario.items():
        print(f"Código: {codigo}, Producto: {datos['Nombre']}, Stock: {datos['Cantidad']}, Precio: ${datos['Precio']:.2f}")

mostrar_inventario()

def actualizar_stock(codigo, cantidad_vendida):
    if codigo in inventario:
        if inventario[codigo]["Cantidad"] >= cantidad_vendida:
            inventario[codigo]["Cantidad"] -= cantidad_vendida
            print(f"✅ Stock actualizado: {inventario[codigo]['Nombre']} → {inventario[codigo]['Cantidad']} unidades restantes.")
        else:
            print(f"⚠️ No hay suficiente stock de {inventario[codigo]['Nombre']}.")
    else:
        print("⚠️ Producto no encontrado.")

# aqui juego con la candidad de carbones de motor que vendemos, puede ser cuatro o cualquier otra cantidad.
# Ejemplo: Vendemos 4 carbones de motor
actualizar_stock("M2", 4)
mostrar_inventario()

# 📌 3️⃣ Usar Tuplas para Tarifas Inmutables
SERVICIOS = (
    ("Copia de llave", 1.00),
    ("Cambio de cuadro de licuadora", 7.50),
    ("Cambio de carbones", 6.50),
    ("Reparación de olla de presión", 10.00)
)

def mostrar_tarifas():
    print("\n💰 Tarifas de Servicios:")
    for servicio in SERVICIOS:
        print(f"Servicio: {servicio[0]}, Precio: ${servicio[1]:.2f}")

mostrar_tarifas()





# ---------------------------------------------------------------------------------------



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







# Estos paso me ayudo a solucionar el problema de tabulate que estaba subrayado con amarillo en forma de sig sag osea esto from tabulate import tabulate y comienza usr python 3.8.10 .
# 🔹 2. Asegura que estás usando el mismo Python en el editor
# Si usas VS Code, revisa en la parte inferior izquierda la versión de Python activa.

# Si es diferente a python3.8.10 (el que usaste antes), cambia el intérprete así:

# Presiona Ctrl + Shift + P
# Escribe "Python: Select Interpreter"
# Selecciona Python 3.8.10 (o la versión donde instalaste tabulate)
# Luego, intenta ejecutar de nuevo el código.