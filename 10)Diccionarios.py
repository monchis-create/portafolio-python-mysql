numbers = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}
print(numbers[2]) #dos

information = {"nombre" : "Carla" ,
               "apellido" : "Perez",
               "edad" : 25,
               "carrera" : "Ingenieria en Sistemas",
               "cursos" : ["Python", "Java", "C++", "JavaScript"]}
print(information["cursos"]) #['Python', 'Java', 'C++', 'JavaScript']
print(information["cursos"][2]) #C++
del information["carrera"]
print(information) #{'nombre': 'Carla', 'apellido': 'Perez', 'edad': 25, 'cursos': ['Python', 'Java', 'C++', 'JavaScript']}
claves = information.keys()
print(claves) #dict_keys(['nombre', 'apellido', 'edad', 'cursos'])
print(type(claves)) #<class 'dict_keys'>
values = information.values()
print(values) #dict_values(['Carla', 'Perez', 25, ['Python', 'Java', 'C++', 'JavaScript']])
pairs = information.items()
print(pairs) #dict_items([('nombre', 'Carla'), ('apellido', 'Perez'), ('edad', 25), ('cursos', ['Python', 'Java', 'C++', 'JavaScript'])])

contact = { "Carla" : {"apellido" : "Perez",
            "edad" : 25,
            "carrera" : "Ingenieria en Sistemas",
            "cursos" : ["Python", "Java", "C++", "JavaScript"]},
            "Diego": {"apellido" : "antezana",
            "edad" : 32,
            "carrera" : "Desarrollador web",
            "cursos" : ["Python", "php", "mysql", "JavaScript"]}
            }

print(contact["Carla"]) #{'apellido': 'Perez', 'edad': 25, 'carrera': 'Ingenieria en Sistemas', 'cursos': ['Python', 'Java', 'C++', 'JavaScript']}

# un ejemplo en la vida real es el ecomerce donde vamos a tener informacion de productos,cada producto  va a tener un nombre una descripcion o un costo, tambien podemos tener informaciones de clientes y mas colecciones de datos.




# Este ejemplo se ve mas ordenado
contact = {"Carla" : {"apellido": "Fernandez",
                      "edad": 23,
                      "Carrera": "Desarrollador web",
                      "Cursos": ["C++", "JavaScript", "Python"]},
           "Diego" : {"apellido": "amadeo",
                      "edad": 34,
                      "Carrera": "ingeniero en sistemas",
                      "Cursos": ["C++", "JavaScript", "Python"]}
                      }

print(contact["Diego"]) #{'apellido': 'amadeo', 'edad': 34, 'Carrera': 'ingeniero en sistemas', 'Cursos': ['C++', 'JavaScript', 'Python']}




#-----------------------------------------------------------------------------------

# Crea un diccionario llamado "estudiantes" donde cada clave sea el nombre de un estudiante y el valor sea otro diccionario con su edad, grado y una lista de materias que está cursando. Luego, imprime la lista de materias de un estudiante específico.

estudiantes = { 
    "Diana": {
        "edad": "15", 
        "grado": "7mo grado", 
        "lista de materias": ["educacion fisica" ," matematica", "lenguaje"] 
    }, 
    "Pablo": {
        "edad": "17", 
        "grado": "6to curso", 
         "lista de materias": ["educacion fisica" , "matematica", "Ciencias Naturales"]  
    }
}

print(estudiantes["Pablo"])


# Obtener todas las claves (nombres de los estudiantes)
print(estudiantes.keys())  

# Obtener todos los valores (información de cada estudiante)
print(estudiantes.values())  

# Obtener los pares clave-valor (nombre del estudiante y su info)
print(estudiantes.items())  

# Si quieres acceder a las materias de cada estudiante usando .items(), puedes hacer algo así:

for nombre, infor in estudiantes.items():
    print(f"{nombre} está cursando: {infor['lista de materias']}")



#-----------------------------------------------------------------------------------



# Crea un diccionario llamado "productos" donde cada clave sea el nombre de un producto y su valor sea otro diccionario con el precio y la cantidad en stock. Luego, escribe un código que te permita obtener el total del valor de todos los productos en stock (precio x cantidad).



productos = {
    "Camiseta": {"precio": 25, "stock": 10},
    "Pantalón": {"precio": 40, "stock": 5},
    "Zapatos": {"precio": 60, "stock": 2}
}

total_valor = 0

# Calculando el total de todos los productos
for producto, info in productos.items():
    total_valor += info["precio"] * info["stock"]

print(f"El valor total de todos los productos en stock es: {total_valor}")


#---------------------------------------------------------------------------------------

# Enunciado del Código
# Desarrolla un programa para gestionar el inventario de productos electrónicos en una tienda. El programa debe permitir lo siguiente:

# 1) Calcular el valor total del inventario:

# La función calcular_valor_total recibe un diccionario con la información del inventario, donde cada producto tiene un precio y un stock. La función debe calcular el valor total del inventario sumando el precio de cada producto multiplicado por su stock disponible.
# El valor total se debe mostrar al inicio, con el inventario inicial.
# 2) Agregar productos al inventario:

# La función agregar_producto permite al usuario agregar un nuevo producto al inventario, pidiendo el nombre, el precio y la cantidad disponible.
# Si el producto ya existe en el inventario, el programa debe indicar que el producto ya está registrado.
# Si el precio o el stock son valores negativos o no numéricos, el programa debe solicitar al usuario que ingrese valores correctos.
# El programa debe preguntar al usuario si desea agregar más productos.
# 3) Mostrar el inventario actualizado:

# Después de agregar los productos, el programa debe mostrar el valor total actualizado del inventario.
# También debe mostrar el inventario actualizado con los nombres de los productos, sus precios y cantidades.
# 4) Uso de Comprehensions:

# Se deben utilizar Dictionary Comprehension para generar el inventario actualizado de forma compacta.
# Se debe usar List Comprehension para imprimir el inventario de manera eficiente.
# Detalles del Código:
# Dictionary Comprehension se usa para generar un nuevo diccionario con los detalles del inventario (precio y stock de cada producto).
# List Comprehension se emplea para imprimir los detalles del inventario en la pantalla de forma compacta.
# Flujo de Ejecución:
# Inicio: El valor total del inventario inicial es calculado y mostrado.
# Agregar Producto: El usuario puede agregar productos con nombre, precio y stock. Se repite este proceso hasta que el usuario decida no agregar más productos.
# Finalización: El valor total del inventario actualizado se muestra, y luego el inventario completo es mostrado en formato compactado.







def calcular_valor_total(ferreteria):
    """Calcula el valor total del inventario usando Dictionary Comprehension."""
    return sum(info["precio"] * info["stock"] for info in ferreteria.values())

# Inventario inicial con productos electrónicos
electronica = {
    "smartphone": {"precio": 300.00, "stock": 50},
    "laptop": {"precio": 800.00, "stock": 30},
    "auriculares": {"precio": 50.00, "stock": 100}
}

print(f"El valor total del inventario es: ${calcular_valor_total(electronica):.2f}")

def agregar_producto():
    """Permite al usuario agregar un nuevo producto al inventario."""
    nuevo_producto = input("Ingresa tu nuevo producto: ").strip().lower()
    
    if nuevo_producto in electronica:
        print("❌ El producto ya existe. Intenta con otro nombre.")
        return
    
    try:
        precio = float(input("Ingresa el precio por unidad: "))
        stock = int(input("Ingresa la cantidad: "))

        if precio < 0 or stock < 0:
            print("❌ El precio y el stock deben ser números positivos.")
            return

        # Agregar el producto al inventario
        electronica[nuevo_producto] = {"precio": precio, "stock": stock}

    except ValueError:
        print("❌ Ingresa valores numéricos válidos.")

# Agregar múltiples productos usando List Comprehension
while True:
    agregar_producto()
    if input("¿Deseas agregar otro producto? (si/no): ").strip().lower() != "si":
        break

# Mostrar el valor total actualizado y el inventario
print(f"\nEl valor total del inventario actualizado es: ${calcular_valor_total(electronica):.2f}")

# 📌 Usamos Dictionary Comprehension para mostrar el inventario actualizado
inventario_actualizado = {producto: f"Precio ${info['precio']}, Stock {info['stock']} Unidades" 
                          for producto, info in electronica.items()}

# 📌 Usamos List Comprehension para imprimirlo de forma compacta
print("\nInventario actualizado:")
[print(f"{producto}: {detalle}") for producto, detalle in inventario_actualizado.items()]


#---------------------------------------------------------------------------------------











# Ejercicio: Registro de ventas en una tienda
# Tienes un diccionario llamado tienda que contiene productos con su precio y stock disponible.
# Debes escribir un código en Python que haga lo siguiente:

# Mostrar todos los productos disponibles en la tienda con su precio y stock.
# Pedir al usuario que ingrese el nombre de un producto que desea comprar.
# Pedir la cantidad que desea comprar.
# Verificar si hay suficiente stock.
# Si hay suficiente stock, restar la cantidad comprada y mostrar el total a pagar.
# Si no hay suficiente stock, mostrar un mensaje diciendo que no hay suficiente.
# Mostrar el inventario actualizado después de la compra.
# Ejemplo de ejecución:
# Productos disponibles:
# manzana - Precio: $1.00 - Stock: 10
# banana - Precio: $0.50 - Stock: 5
# naranja - Precio: $0.75 - Stock: 8

# ¿Qué producto deseas comprar? banana
# ¿Cuántas unidades deseas comprar? 3

# Total a pagar: $1.50
# Inventario actualizado:
# manzana - Precio: $1.00 - Stock: 10
# banana - Precio: $0.50 - Stock: 2
# naranja - Precio: $0.75 - Stock: 8
# 🔍 Pistas:

# Usa un input() para preguntar qué producto comprar.
# Asegúrate de verificar si hay suficiente stock antes de restar.
# Multiplica el precio por la cantidad comprada para obtener el total a pagar.
# 🔥 ¡A ver cómo lo resuelves! Luego me muestras tu código para revisarlo. 😏







# Tú dijiste:
# esta dificil este ejercicio dame la solucion
# ChatGPT Plus
# ¡Aquí tienes la solución al ejercicio! 😃

# Diccionario con productos, precios y stock
tienda = {
    "manzana": {"precio": 1.00, "stock": 10},
    "banana": {"precio": 0.50, "stock": 5},
    "naranja": {"precio": 0.75, "stock": 8}
}

# Mostrar productos disponibles
print("Productos disponibles:")
for producto, info in tienda.items():
    print(f"{producto} - Precio: ${info['precio']} - Stock: {info['stock']}")

# Pedir al usuario que ingrese el producto y cantidad
producto_comprar = input("\n¿Qué producto deseas comprar? ").lower()

if producto_comprar in tienda:
    cantidad = int(input("¿Cuántas unidades deseas comprar? "))

    # Verificar si hay suficiente stock
    if cantidad <= tienda[producto_comprar]["stock"]:
        total_pagar = cantidad * tienda[producto_comprar]["precio"]
        tienda[producto_comprar]["stock"] -= cantidad  # Restar stock

        print(f"\nTotal a pagar: ${total_pagar:.2f}")
        print("\nInventario actualizado:")
        for producto, info in tienda.items():
            print(f"{producto} - Precio: ${info['precio']} - Stock: {info['stock']}")
    else:
        print("\nNo hay suficiente stock para esa cantidad. 😞")
else:
    print("\nEse producto no está en la tienda. 😢")

# Explicación del código:
# Creamos el diccionario tienda con los productos, sus precios y el stock disponible.
# Mostramos todos los productos con su precio y stock.
# Pedimos al usuario que ingrese el nombre del producto que quiere comprar.
# Verificamos si el producto existe en la tienda.
# Pedimos la cantidad a comprar y verificamos si hay suficiente stock.
# Si hay suficiente stock, calculamos el total a pagar y restamos la cantidad comprada del inventario.
# Si no hay suficiente stock, mostramos un mensaje de error.
# 📌 Prueba el código y dime si funciona bien! 😏