x=5
if x > 5 :
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else :
    print("x es menor que 5")
print("afuera")



# -------------------------------------------------------------------------------------------------------



x=15
y=25


# Con el and, ambas condiciones deben ser verdaderas para que se cumpla. Es decir, x > 10 y y > 25 deben ser verdaderos. 😎
# if x > 10 and y >= 25:
if x > 10 and y > 5:
    print("x es mayor que 10 y y es mayor que 15")

# cualquiera de las dos puede ser verdadera o ambas a la vez para que se cumpla la condición
if x > 10 or y > 25:
    print("x es mayor que 10 o y es mayor que 25")


if not x > 10:
    print("x no es mayor que 10")



# --------------------------------------------------------------------------------------------------------



is_member = True
age = 15


if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")

# Salida: Tienes acceso ya que eres miembro y mayor o igual a 15 años







is_member = False
age = 15


if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")

# Salida: No eres miembro y NO TIENES ACCESO








is_member = True
age = 11


if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")

# Salida: No tienes acceso ya que eres miembro pero menor a 15 años






























# esto son las escturcturas condicionales anidadas que se pueden hacer en python                          
# Precios de los servicios
precios = {
    1: ("Copia de llave", 8),
    2: ("Cambio de cuadro de licuadora", 7.50),
    3: ("ABC", 7.50),
    4: ("Cambio de carbones", 6.50)
}

# Mostrar opciones
print("Servicios disponibles:")
for num, (servicio, precio) in precios.items():
    print(f"{num}. {servicio} (${precio})")

# Pedir selección al usuario
opciones = input("Ingrese los números de los servicios que desea, separados por comas: ")

# Convertir entrada a lista de números
opciones = [int(x.strip()) for x in opciones.split(",") if x.strip().isdigit()]

# Calcular total
total = 0
print("\nServicios seleccionados:")
for opcion in opciones:
    if opcion in precios:
        servicio, precio = precios[opcion]
        print(f"- {servicio}: ${precio}")
        total += precio
    else:
        print(f"- Opción {opcion} no es válida.")

print(f"\nTotal a pagar: ${total}")
print("¡Gracias por su visita!")










































































#  Esto es con descuentos
# Precios de los servicios
precios = {
    1: ("Copia de llave", 1),
    2: ("Cambio de cuadro de licuadora", 7.50),
    3: ("ABC", 7.50),
    4: ("Cambio de carbones", 6.50)
}

# Mostrar opciones
print("Servicios disponibles:")
for num, (servicio, precio) in precios.items():
    print(f"{num}. {servicio} (${precio})")

# Pedir selección al usuario
opciones = input("Ingrese los números de los servicios que desea, separados por comas: ")
opciones = [int(x.strip()) for x in opciones.split(",") if x.strip().isdigit()]

# Calcular total sin descuentos
total = 0
print("\nServicios seleccionados:")
for opcion in opciones:
    if opcion in precios:
        servicio, precio = precios[opcion]
        print(f"- {servicio}: ${precio}")
        total += precio
    else:
        print(f"- Opción {opcion} no es válida.")

# Mostrar total antes del descuento
print(f"\nTotal antes del descuento: ${total}")

# Aplicar descuentos usando if, elif y else
descuento = 0
if 2 in opciones and 4 in opciones:
    descuento = 2
    print("Descuento aplicado: -$2 por elegir 'Cambio de cuadro de licuadora' y 'Cambio de carbones'.")
elif 1 in opciones and 3 in opciones:
    descuento = 0.50
    print("Descuento aplicado: -$0.50 por elegir 'Copia de llave' y 'ABC'.")
else:
    print("No hay descuentos aplicables.")

# Calcular total final con descuento
total_final = total - descuento

# Mostrar total final después del descuento
print(f"\nTotal a pagar después del descuento: ${total_final}")
print("¡Gracias por su visita!")