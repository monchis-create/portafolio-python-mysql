a = [1,2,3,4,5]
b = a
print(a) #[1, 2, 3, 4, 5]
print(b) #[1, 2, 3, 4, 5]
del a[0] # aqui estoy especificando que quiero eliminar un elemento de la lista a , pero esta modificacion se esta realizando en ambas variables, esto sucede por que apuntan al mismo espacio en memoria.
print(a) #[2, 3, 4, 5]
print(b) #[2, 3, 4, 5]
# para ver a donde es que se esta almacenando esta informacion le voy a preguntar cual es el id en memoria , entonces escribimos la funcion id.

print(id(a)) #140655178576640
print(id(b)) #140655178576640

#para no tener este problema de que todas las acciones que haga en una variable se vean reflejadas en otras , lo que tengo que crear es slaicing.

# aqui empieza el slaicing
c = a[:]# va desde la posicion cero , hasta la posicion final [:]
print(id(a)) #140655178576640
print(id(b)) #140655178576640
print(id(c)) #140655178576064
a.append(6)
print(a) #[2, 3, 4, 5, 6]
print(b) #[2, 3, 4, 5, 6]
print(c) #[2, 3, 4, 5]

#-------------------------------------------------------------------------------------------




# Este esta todo echo un rebulicio no me sirve . El ultimo esta mucho mas ordenado y organizado que el antepenultimo.

# 1️⃣ Copiar pedidos sin afectar la lista original
# Si quieres hacer un respaldo de los pedidos antes de modificarlos:


pedidos = [
    {"servicio": "Copia de llave", "precio": 1},
    {"servicio": "Cambio de cuadro de licuadora", "precio": 7.50},
    {"servicio": "Cambio de carbones", "precio": 6.50},
    {"servicio": "Reparación de olla de presión", "precio": 10.00}
]

# Crear una copia de los pedidos antes de modificarlos
pedidos_backup = pedidos[:]

# Modificar la lista original
pedidos.append({"servicio": "ABC", "precio": 7.50})

print("Pedidos originales:", pedidos)
print("Pedidos backup:", pedidos_backup)  # No se modificó
# 💡 Útil para evitar perder información si necesitas hacer cambios en la lista de pedidos.

# 2️⃣ Extraer solo ciertos tipos de servicios
# Si quieres ver solo los primeros 3 pedidos del día, puedes usar slicing:


pedidos_del_dia = pedidos[:3]  # Extrae los primeros 3 pedidos
print("Pedidos del día:", pedidos_del_dia)
# 💡 Útil si quieres ver solo los primeros clientes atendidos.

# 3️⃣ Invertir la lista para ver los pedidos más recientes
# Si deseas ver los últimos pedidos primero, puedes invertir la lista con slicing:


pedidos_recientes = pedidos[::-1]  # Invierte la lista
print("Pedidos más recientes primero:", pedidos_recientes)
# 💡 Útil si necesitas ver los últimos pedidos sin reordenar la lista original.

# 4️⃣ Extraer pedidos con paso (por ejemplo, cada 2 pedidos)
# Si quieres ver solo los pedidos en posiciones pares (0, 2, 4...), usa slicing con paso:


pedidos_pares = pedidos[::2]
print("Pedidos en posiciones pares:", pedidos_pares)
# 💡 Útil para revisar pedidos específicos o dividirlos en turnos.

# 5️⃣ Manejo de nombres de clientes o códigos de servicio
# Si tienes códigos de servicio y necesitas solo una parte:


codigo = "LIC-12345"  # Código de un servicio de licuadora
codigo_solo_numeros = codigo[4:]  # Extrae solo los números
print(codigo_solo_numeros)  # "12345"
# 💡 Útil para extraer información relevante sin necesidad de procesar todo el texto.

# 📌 ¿Cómo te sirve esto en tu negocio?
# ✔️ Respaldar datos antes de hacer cambios.
# ✔️ Revisar solo algunos pedidos sin modificar la lista completa.
# ✔️ Ordenar y organizar la información fácilmente.






#-------------------------------------------------------------------------------------------


# Codigo mejorado con slicing  sangrias y saltos de linea, pero aun sigue sucio se podria decir que esta un poco mejor que el que esta arriba. 

import copy
from pprint import pprint

pedidos = [
    {"servicio": "Copia de llave", "precio": 1},
    {"servicio": "Cambio de cuadro de licuadora", "precio": 7.50},
    {"servicio": "Cambio de carbones", "precio": 6.50},
    {"servicio": "Reparación de olla de presión", "precio": 10.00}
]

def copiar_pedidos(pedidos):
    """Devuelve una copia independiente de la lista de pedidos."""
    return copy.deepcopy(pedidos)

def extraer_pedidos(pedidos, cantidad=3):
    """Devuelve los primeros 'cantidad' pedidos."""
    return pedidos[:cantidad]

def invertir_pedidos(pedidos):
    """Devuelve los pedidos en orden inverso."""
    return pedidos[::-1]

def extraer_pares(pedidos):
    """Devuelve solo los pedidos en posiciones pares."""
    return pedidos[::2]

def extraer_codigo_numerico(codigo):
    """Extrae los números de un código de servicio."""
    return codigo.split('-')[-1]  # Más flexible si cambia el formato

# Uso de funciones
pedidos_backup = copiar_pedidos(pedidos)
pedidos.append({"servicio": "ABC", "precio": 7.50})

print("\n📌 Pedidos originales:")
pprint(pedidos)
print("\n📌 Pedidos backup (sin cambios):")
pprint(pedidos_backup)

print("\n📌 Pedidos del día:")
pprint(extraer_pedidos(pedidos))

print("\n📌 Pedidos recientes primero:")
pprint(invertir_pedidos(pedidos))

print("\n📌 Pedidos en posiciones pares:")
pprint(extraer_pares(pedidos))

codigo = "LIC-12345"
print("\n📌 Código extraído:", extraer_codigo_numerico(codigo))





#----------------------------------------------------------------------------------------




# Codigo mucho mejor mejorado con slicing  sangrias y saltos de linea mejor que el que esta arriba , mas limpio y ordenado.


import copy
import json

pedidos = [
    {"servicio": "Copia de llave", "precio": 1},
    {"servicio": "Cambio de cuadro de licuadora", "precio": 7.50},
    {"servicio": "Cambio de carbones", "precio": 6.50},
    {"servicio": "Reparación de olla de presión", "precio": 10.00}
]

def copiar_pedidos(pedidos):
    """Devuelve una copia independiente de la lista de pedidos."""
    return copy.deepcopy(pedidos)

def extraer_pedidos(pedidos, cantidad=3):
    """Devuelve los primeros 'cantidad' pedidos."""
    return pedidos[:cantidad]

def invertir_pedidos(pedidos):
    """Devuelve los pedidos en orden inverso."""
    return pedidos[::-1]

def extraer_pares(pedidos):
    """Devuelve solo los pedidos en posiciones pares."""
    return pedidos[::2]

def extraer_codigo_numerico(codigo):
    """Extrae los números de un código de servicio."""
    return codigo.split('-')[-1]  # Más flexible si cambia el formato

# Uso de funciones
pedidos_backup = copiar_pedidos(pedidos)
pedidos.append({"servicio": "ABC", "precio": 7.50})

def imprimir_pedidos(pedidos, titulo):
    print(f"\n📌 {titulo}:")
    for pedido in pedidos:
        print(f"  Servicio: {pedido['servicio']}, Precio: {pedido['precio']}")

imprimir_pedidos(pedidos, "Pedidos originales")
imprimir_pedidos(pedidos_backup, "Pedidos backup (sin cambios)")
imprimir_pedidos(extraer_pedidos(pedidos), "Pedidos del día")
imprimir_pedidos(invertir_pedidos(pedidos), "Pedidos recientes primero")
imprimir_pedidos(extraer_pares(pedidos), "Pedidos en posiciones pares")

codigo = "LIC-12345"
print("\n📌 Código extraído:", extraer_codigo_numerico(codigo))
#----------------------------------------------------------------------------------------

