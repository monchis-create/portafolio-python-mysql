text = "Hola mundo"
pos = text.index("mundo")
print(pos)  # Devuelve 5, que es el índice donde comienza "mundo"


# ---------------------------------------------------------------------------------------------


# El método str.isalnum() verifica si todos los caracteres de una cadena son alfanuméricos (letras o números) y si la cadena no está vacía.
# Si contiene espacios, símbolos o está vacía, devuelve False.
# Por ejemplo: "Hola123".isalnum() devuelve True, pero "Hola 123".isalnum() devuelve False.

text = "Hola123"
print(text.isalnum())  # Devuelve True porque solo tiene letras y números


# ----------------------------------------------------------------------------------------------


# str.isalpha() verifica si una cadena contiene solo letras y no está vacía.
# Devuelve True si no hay números, espacios ni símbolos.
# Por ejemplo: "Hola".isalpha() es True, pero "Hola 123".isalpha() es False.
print("Hola".isalpha())  # Devuelve True porque todos los caracteres son letras


# --------------------------------------------------------------------------------------------


print("Hello!".isascii())  # Devuelve True porque todos los caracteres son ASCII
print("¡Hola!".isascii())  # Devuelve False porque "¡" no es un carácter ASCII



# --------------------------------------------------------------------------------------------




print("123".isdecimal())  # Devuelve True porque todos los caracteres son números enteros
print("123.45".isdecimal())  # Devuelve False porque contiene un punto



# --------------------------------------------------------------------------------------------



print("123".isdigit())  # Devuelve True porque todos los caracteres son dígitos
print("²³".isdigit())  # Devuelve True porque son dígitos especiales (superíndices)
print("123a".isdigit())  # Devuelve False porque contiene una letra


# --------------------------------------------------------------------------------------------


print("variable".isidentifier())  # Devuelve True, es un identificador válido
print("123variable".isidentifier())  # Devuelve False, no puede empezar por un número
print("variable123".isidentifier()) # Devuelve True, puede contener números


# --------------------------------------------------------------------------------------------



print("hola".islower())  # Devuelve True porque todos los caracteres están en minúsculas
print("Hola".islower())  # Devuelve False porque contiene una mayúscula
 
# --------------------------------------------------------------------------------------------


print("123".isnumeric())  # Devuelve True porque todos los caracteres son numéricos
print("½".isnumeric())  # Devuelve True porque es un carácter numérico (fracción vulgar)
print("123a".isnumeric())  # Devuelve False porque contiene una letra


# --------------------------------------------------------------------------------------------



print("Hola mundo!".isprintable())  # Devuelve True porque todos los caracteres son imprimibles
print("Hola\nmundo!".isprintable())  # Devuelve False porque '\n' no es un carácter imprimible


# --------------------------------------------------------------------------------------------

print("   ".isspace())  # Devuelve True porque solo contiene espacios en blanco
print("Hola mundo".isspace())  # Devuelve False porque tiene caracteres no espacios


# --------------------------------------------------------------------------------------------



print("Hola Mundo".istitle())  # Devuelve True porque está en formato título
print("hola Mundo".istitle())  # Devuelve False porque la primera palabra no empieza con mayúscula


# --------------------------------------------------------------------------------------------



print("HOLA".isupper())  # Devuelve True porque todos los caracteres están en mayúsculas
print("Hola".isupper())  # Devuelve False porque contiene minúsculas

# --------------------------------------------------------------------------------------------


print(", ".join(["manzana", "banana", "pera"]))  # Devuelve 'manzana, banana, pera'

# --------------------------------------------------------------------------------------------

print("Hola".ljust(10, '-'))  # Devuelve 'Hola------' (rellena con '-')


# --------------------------------------------------------------------------------------------


print("HOLA MUNDO".lower())  # Devuelve 'hola mundo'

# --------------------------------------------------------------------------------------------





# ¿Para qué sirve?
# Este tipo de código es útil para tareas como:

# Encriptar textos simples. 
# Sustituir caracteres en cadenas de texto según ciertas reglas.
# Normalizar o transformar textos en aplicaciones (como cambiar vocales por números para jugar con palabras o implementar cifrados básicos).




# Crear una tabla de traducción
tabla = str.maketrans("aeiou", "12345")

# Usar la tabla con translate
texto = "hola mundo"
resultado = texto.translate(tabla)

print(resultado)

# salida = h4l1 m5nd4


# --------------------------------------------------------------------------------------------



texto = "hola mundo"
resultado = texto.partition(" ")
print(resultado)  

# salida
('hola', ' ', 'mundo')

# --------------------------------------------------------------------------------------------


# esto removeprefix solo esta disponible para python 3.9 y yo tengo el 3.8
texto = "PythonEsGenial"
resultado = texto.removeprefix("Python")
print(resultado) # Salida: EsGenial
# Salida:
# EsGenial
# Explicación breve:
# Si texto comienza con "Python", se elimina ese prefijo. De lo contrario, no cambia.


# --------------------------------------------------------------------------------------------


# Esto no me va a funcionar con una version menor a 3.9 y yo tengo el 3.8
texto = "holamundo"
resultado = texto.removesuffix("mundo")
print(resultado)

# Salida:
# hola


# --------------------------------------------------------------------------------------------


# Aqui me va a cambiar la palabra mundo por la palabra planeta


# Declaramos un string
texto = "Hola mundo, mundo increíble, mundo único"

# Reemplazamos todas las palabras de "mundo" por "planeta"
resultado_1 = texto.replace("mundo", "planeta")

# Reemplazamos solo las dos primeras palabras de "mundo" por "planeta"
resultado_2 = texto.replace("mundo", "planeta", count=2)

print("Texto original:", texto)        # Salida: Hola mundo, mundo increíble, mundo único
print("Reemplazo total:", resultado_1) # Salida: Hola planeta, planeta increíble, planeta único
print("Reemplazo parcial (2 ocurrencias):", resultado_2) # Salida: Hola planeta, planeta increíble, mundo único








texto = "hola mundo, mundo bonito"
resultado = texto.replace("mundo", "planeta")
print(resultado)
# Salida:
# hola planeta, planeta bonito