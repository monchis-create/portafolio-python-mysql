numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aqui i es igual a: " , i+1)


for i in range(3, 10):
    print (i)



fruits = ["manzana", "pera", "uva", "naranja", "tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "naranja":
        print("naranja encontrada")




x=0
while x < 5:
    if x==3:
        break
    print("x es igual a: ", x)
    x += 1





numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i == 3:
        continue
    print("Aqui i es igual a: " , i)




    numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i == 3:
        break
    print("Aqui i es igual a: " , i)






# ----------------------------------------------------------------------------------------------------





servicios = {
    "Copias de llaves": 1.00,
    "Cambio de cuadro de licuadora": 7.50,
    "ABC": 7.50,
    "Cambio de carbones": 6.50
}

print("Servicios disponibles:")
for servicio, precio in servicios.items():
    print(f"- {servicio}: ${precio}")






total = 0
while True:
    print("\nIngrese el servicio (o 'salir' para finalizar): ")
    servicio = input("> ")
    
    if servicio.lower() == "salir":
        break
    
    if servicio in servicios:
        total += servicios[servicio]
        print(f"{servicio} agregado. Total: ${total:.2f}")
    else:
        print("Servicio no encontrado. Intente de nuevo.")

print(f"\nTotal a pagar: ${total:.2f}")







for servicio in servicios:
    if servicio == "ABC":
        continue  # Salta este servicio
    print(f"Disponible: {servicio} - ${servicios[servicio]}")









for servicio in servicios:
    if servicio == "Cambio de cuadro de licuadora":
        print("Este servicio no está disponible por ahora.")
        break
    print(f"Servicio: {servicio} - ${servicios[servicio]}")
















monto_recibido = float(input("\nIngrese el dinero recibido: $"))
cambio = monto_recibido - total

if cambio < 0:
    print(f"Falta dinero. Aún debe ${-cambio:.2f}")
else:
    print(f"Cambio a devolver: ${cambio:.2f}")









#-----------------------------------------------------------------------------------------


# codigo mejorado
servicios = {
    "Copias de llaves": 1.00,
    "Cambio de cuadro de licuadora": 7.50,
    "ABC": 7.50,
    "Cambio de carbones": 6.50,
    "Cambio de switch": 10.00,
    "Arreglo de placha de ropa": 10.00
}

def mostrar_servicios():
    """Muestra todos los servicios disponibles."""
    print("\nServicios disponibles:")
    for servicio, precio in servicios.items():
        print(f"- {servicio}: ${precio:.2f}")

def calcular_total():
    """Calcula el total según los servicios ingresados por el usuario."""
    total = 0
    while True:
        servicio = input("\nIngrese el servicio (o 'salir' para finalizar): ").strip().lower()
        
        if servicio == "salir":
            break
        
        # Buscar el servicio sin importar mayúsculas/minúsculas
        encontrado = False
        for nombre_servicio in servicios.keys():
            if nombre_servicio.lower() == servicio:
                total += servicios[nombre_servicio]
                print(f"{nombre_servicio} agregado. Total: ${total:.2f}")
                encontrado = True
                break
        
        if not encontrado:
            print("Servicio no encontrado. Intente de nuevo.")
    
    return total

def procesar_pago(total):
    """Solicita el dinero al usuario y calcula el cambio."""
    while True:
        try:
            monto_recibido = float(input("\nIngrese el dinero recibido: $"))
            cambio = monto_recibido - total
            
            if cambio < 0:
                print(f"Falta dinero. Aún debe ${-cambio:.2f}")
            else:
                print(f"Cambio a devolver: ${cambio:.2f}")
                break
        except ValueError:
            print("Por favor, ingrese un monto válido.")

# Ejecutar funciones en orden
mostrar_servicios()  # Muestra todos los servicios disponibles
total = calcular_total()
print(f"\nTotal a pagar: ${total:.2f}")
procesar_pago(total)





# ----------------------------------------------------------------------------------------------------




# codigo mejorado con el tabulate 


from tabulate import tabulate

servicios = {
    "Copias de llaves": 1.00,
    "Cambio de cuadro de licuadora": 7.50,
    "ABC": 7.50,
    "Cambio de carbones": 6.50,
    "Cambio de switch": 10.00,
    "Arreglo de plancha de ropa": 10.00
}

def mostrar_servicios():
    """Muestra todos los servicios disponibles en formato de tabla."""
    tabla = [[servicio, f"${precio:.2f}"] for servicio, precio in servicios.items()]
    print("\nServicios disponibles:")
    print(tabulate(tabla, headers=["Servicio", "Precio"], tablefmt="grid"))

def calcular_total():
    """Calcula el total según los servicios ingresados por el usuario."""
    total = 0
    while True:
        servicio = input("\nIngrese el servicio (o 'salir' para finalizar): ").strip().lower()
        
        if servicio == "salir":
            break
        
        # Buscar el servicio sin importar mayúsculas/minúsculas
        encontrado = False
        for nombre_servicio in servicios.keys():
            if nombre_servicio.lower() == servicio:
                total += servicios[nombre_servicio]
                print(f"{nombre_servicio} agregado. Total: ${total:.2f}")
                encontrado = True
                break
        
        if not encontrado:
            print("Servicio no encontrado. Intente de nuevo.")
    
    return total

def procesar_pago(total):
    """Solicita el dinero al usuario y calcula el cambio."""
    while True:
        try:
            monto_recibido = float(input("\nIngrese el dinero recibido: $"))
            cambio = monto_recibido - total
            
            if cambio < 0:
                print(f"Falta dinero. Aún debe ${-cambio:.2f}")
            else:
                print(f"Cambio a devolver: ${cambio:.2f}")
                break
        except ValueError:
            print("Por favor, ingrese un monto válido.")

# Ejecutar funciones en orden
mostrar_servicios()  # Muestra todos los servicios en tabla
total = calcular_total()
print(f"\nTotal a pagar: ${total:.2f}")
procesar_pago(total)





# ----------------------------------------------------------------------------------------------------



#  codigo mejorado.
from tabulate import tabulate

servicios = {
    "Copias de llaves": 1.00,
    "Cambio de cuadro de licuadora": 7.50,
    "ABC": 7.50,
    "Cambio de carbones": 6.50,
    "Cambio de switch": 10.00,
    "Arreglo de plancha de ropa": 10.00
}

def mostrar_servicios():
    """Muestra todos los servicios disponibles en formato de tabla."""
    tabla = [[servicio, f"${precio:.2f}"] for servicio, precio in servicios.items()]
    print("\nServicios disponibles:")
    print(tabulate(tabla, headers=["Servicio", "Precio"], tablefmt="grid"))

def calcular_total():
    """Calcula el total según los servicios ingresados por el usuario."""
    total = 0
    while True:
        servicio = input("\nIngrese el servicio (o 'salir' para finalizar): ").strip().lower()
        
        if servicio == "salir":
            break
        
        # Buscar el servicio sin importar mayúsculas/minúsculas
        encontrado = False
        for nombre_servicio in servicios.keys():
            if nombre_servicio.lower() == servicio:
                total += servicios[nombre_servicio]
                print(f"{nombre_servicio} agregado. Total: ${total:.2f}")
                encontrado = True
                break
        
        if not encontrado:
            print("Servicio no encontrado. Intente de nuevo.")
            continue  # Continúa el bucle sin seguir ejecutando más código
    
    return total

def procesar_pago(total):
    """Solicita el dinero al usuario y calcula el cambio."""
    while True:
        try:
            monto_recibido = float(input("\nIngrese el dinero recibido: $"))
            cambio = monto_recibido - total
            
            if cambio < 0:
                print(f"Falta dinero. Aún debe ${-cambio:.2f}")
                continue  # Si falta dinero, vuelve a solicitar el monto
            else:
                print(f"Cambio a devolver: ${cambio:.2f}")
                break
        except ValueError:
            print("Por favor, ingrese un monto válido.")
            continue  # Vuelve a solicitar el monto si la entrada no es válida

# Ejecutar funciones en orden
mostrar_servicios()  # Muestra todos los servicios en tabla
total = calcular_total()
print(f"\nTotal a pagar: ${total:.2f}")
procesar_pago(total)
