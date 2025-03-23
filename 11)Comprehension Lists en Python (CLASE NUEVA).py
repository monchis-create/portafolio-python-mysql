# Elevar al cuadrado los números del 1 al 10
squares = [x**2 for x in range(1,11)]
print("Cuadrados:", squares) #Cuadrados: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#aqui la profe se equivoco porque es suma y no multiplicacion en el 32 ya lo corregi.
celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Temperatura en F:" ,fahrenheit)  #Temperatura en F: [32.0, 50.0, 68.0, 86.0, 104.0] 
#Temperatura en F: [0.0, 576.0, 1152.0, 1728.0, 2304.0]


#numeros pares del 1 al 20
# [expresión for elemento in iterable if condición]
evens = [x for x in range(1,21) if x%2 ==0]
print(evens) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposed) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Imagina que tienes una tabla con ventas de helados:

#          Lunes	Martes	Miércoles
# Fresa	    10	       15	    20
# Chocolate	5	       8	    12
# Vainilla	7	       9	    14
# Así está organizada por sabores. Pero, ¿y si quieres verla por días en vez de sabores?

# Al usar el código para transponer, la tabla cambia a:

#                Fresa	Chocolate	Vainilla
# Lunes	            10	    5	       7
# Martes	        15	    8	       9
# Miércoles	        20	    12	       14
# Así ahora puedes ver cuántos helados se vendieron cada día, en vez de por sabor. Es como girar la tabla para ver los datos de otra manera. ¡Eso es transponer! 🍦📊

# ------------------------------------------------------------------------------------------------------



# Resumen
# Una Comprehension List es una forma concisa de crear listas en Python, pues permite generar listas nuevas transformando cada elemento de una colección existente o creando elementos a partir de un rango. La sintaxis es compacta y directa, lo que facilita la comprensión del propósito de tu código de un vistazo.

# La estructura básica de una Comprehension List es:

# [expresión for elemento in iterable if condición]
# Que se traduce a: “Crea una nueva lista evaluando nueva_expresión para cada elemento en el iterable.”

# Ejercicios:
# 1) Doble de los Números
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.

# 1) Doble de los Números

# pythonCopiar código
# [expresión for elemento in iterable if condición]
numeros = [1, 2, 3, 4, 5]
dobles = [x * 2 for x in numeros]
print("Dobles:", dobles)   #Dobles: [2, 4, 6, 8, 10]



# 2) Filtrar y Transformar en un Solo Paso
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

# 2) Filtrar y Transformar en un Solo Paso
# [expresión for elemento in iterable if condición]
# pythonCopiar código
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print("Palabras filtradas y en mayúsculas:", palabras_filtradas)    #Palabras filtradas y en mayúsculas: ['MONTAÑA', 'ESTRELLA']








# 3) Crear un Diccionario con List Comprehension
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.


# 3) Crear un Diccionario con List Comprehension
# [expresión for elemento in iterable if condición]
# pythonCopiar código
claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {claves[i]: valores[i] for i in range(len(claves))}
print("Diccionario creado:", diccionario)   #Diccionario creado: {'nombre': 'Juan', 'edad': 30, 'ocupación': 'Ingeniero'}


# 4) Anidación de List Comprehensions
# Dada una lista de listas (una matriz):

# pythonCopiar código
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.


# 4) Anidación de List Comprehensions
# [expresión for elemento in iterable if condición]
# pythonCopiar código
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta_comprehension = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("Transpuesta con List Comprehension:", transpuesta_comprehension) #Transpuesta con List Comprehension: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 5) Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:

# pythonCopiar código
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

# 5) Extraer Información de una Lista de Diccionarios
# [expresión for elemento in iterable if condición]

# pythonCopiar código
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid)  #Nombres de personas en Madrid mayores de 30 años: ['Ana', 'Laura']

# 6) List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

# 6) List Comprehension con un else
# [expresión for elemento in iterable if condición]

# 6. List Comprehension con un else
# La sintaxis de List Comprehension con un else es [expresión if condición else expresión for elemento in iterable]. En este ejemplo, se crea una lista que contiene los cuadrados de los números pares y el número mismo si es impar. 

# pythonCopiar código
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros]  #Si el número es par, se multiplica por 2, si es impar, se deja igual.
print("Números transformados:", transformados) #Números transformados: [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]


# Soluciones

# Las Comprehension Lists en Python son una herramienta poderosa y versátil que permite escribir código más limpio y eficiente. Al dominar su uso, puedes realizar transformaciones y filtrados de datos de manera más concisa, lo que no solo mejora la legibilidad del código, sino que también puede optimizar su rendimiento.

# Practicar con ejemplos como los presentados te ayudará a integrar esta técnica en tus proyectos de programación diaria, facilitando la manipulación de colecciones de datos de manera elegante y efectiva.







# Crea una lista que contenga los cuadrados de los números del 1 al 20, pero solo si el número es múltiplo de 3.

cuadrados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

listas_de_cuadrados = [x**2 for x in cuadrados if x % 3 == 0]
print(listas_de_cuadrados) #[9, 36, 81, 144, 225, 324]

listas_de_cuadrados = [x**2 for x in range(1,21) if x % 3 == 0]
print(listas_de_cuadrados) #[9, 36, 81, 144, 225, 324]




# Crear combinaciones entre dos listas.
nombres = ["Moisés", "Juan", "Pedro"]
apellidos = ["López", "García", "Pérez"]
combinaciones = [f"{n} {a}" for n in nombres for a in apellidos]
print(combinaciones) #['Moisés López', 'Moisés García', 'Moisés Pérez', 'Juan López', 'Juan García', 'Juan Pérez', 'Pedro López', 'Pedro García', 'Pedro Pérez']







# 7. Extraer vocales de una palabra
# 📌 Ejemplo: Filtrar solo vocales de una palabra.


palabra = "comprensión"
vocales = [letra for letra in palabra if letra in "aeiou"]
print(vocales)
# 📌 Salida: ['o', 'e', 'i', 'ó']





# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL 
# PARA LA VIDA REAL }

# 2️⃣ Limpiar datos eliminando espacios extra
# Tienes una lista de nombres ingresados con espacios innecesarios y necesitas limpiarlos.

nombres = ["  Moisés ", " Juan ", " Ana  "]  
nombres_limpios = [nombre.strip() for nombre in nombres]  
print(nombres_limpios)  
# ➡️ ['Moisés', 'Juan', 'Ana']






# 5️⃣ Crear una lista de productos con descuento aplicado
# 📌 Ejemplo: Dada una lista de precios, aplicar un 10% de descuento a cada uno.
precios = [100, 200, 300, 400]  
descuento = [p * 0.9 for p in precios]  # Aplicando un 10% de descuento  
print(descuento)  
# ➡️ [90.0, 180.0, 270.0, 360.0]








# Crea una lista que contenga los cuadrados de los números del 1 al 20, pero solo incluye aquellos que sean múltiplos de 4.

lista = [x**2 for x in range(1,21) if x % 4 == 0]
print(lista) #[16, 64, 144, 256, 400]