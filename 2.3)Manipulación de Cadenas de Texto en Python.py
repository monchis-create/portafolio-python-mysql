
# rfind sirve para encontrar la posición de la última aparición de una subcadena en un texto.
texto = "hola auron mundo"
indice = texto.rfind("mundo")
print(indice)              
# Salida:
# 11


texto = "abracadabra"
indice = texto.rfind("abra")
print(indice)
# Salida:
# 7

# --------------------------------------------------------------------------------------------

texto = "hola mundo, hola universo"
posicion = texto.rindex("hola")
print(posicion)  # Salida: 12
# Explicación:
# rindex busca la última aparición de "hola" en la cadena. Si no la encuentra, lanza un ValueError. En este caso, la última aparición de "hola" está en la posición 12  . No cuenta los espacios.

# cuenta de atras para delante
# ----------------------------------------------------------------------------------------------



texto = "hola"
resultado = texto.rjust(10, "-")
print(resultado)  # Salida: ------hola
# Explicación:
# El texto "hola" se justifica a la derecha en una cadena de longitud 10. Los caracteres de relleno son guiones ("-"). Si la longitud especificada fuera menor o igual a la longitud de "hola", se devolvería el texto sin cambios.


# ----------------------------------------------------------------------------------------------




texto = "manzana-pera-mango"
resultado = texto.rpartition("-")
print(resultado)  # Salida: ('manzana-pera', '-', 'mango')
# Explicación:
# El método busca la última ocurrencia del separador "-".

# La primera parte de la tupla contiene el texto antes del separador.
# La segunda parte contiene el separador.
# La tercera parte contiene el texto después del separador.


# Si no se encuentra el separador:

resultado = texto.rpartition("/")
print(resultado)  # Salida: ('', '', 'manzana-pera-mango')



# -----------------------------------------------------------------------------------------------


texto = "manzana pera mango uva"
resultado = texto.rsplit(" ", 2)
print(resultado)  # Salida: ['manzana pera', 'mango', 'uva']
# Explicación como para un niño pequeño:

# Tenemos una lista de palabras separadas por espacios.
# Con rsplit, decimos: "Corta desde el final y haz 2 cortes como máximo".
# El resultado son tres partes: las primeras palabras juntas y luego las últimas dos separadas.
# Si no dices cuántos cortes hacer (maxsplit), separará todo por espacios. 😊




# -----------------------------------------------------------------------------------------------




texto = "hola mundo!!!"
resultado = texto.rstrip("!")
print(resultado)  # Salida: 'hola mundo'
# Explicación:

# rstrip("!") elimina todos los signos de exclamación ("!") del final de la cadena.
# Si no hay más caracteres específicos al final, se detiene.
# Si no especificas nada, quitará solo los espacios en blanco al final:

texto = "hola mundo   "
resultado = texto.rstrip()
print(resultado)  # Salida: 'hola mundo'




# -----------------------------------------------------------------------------------------------




texto = "manzana,pera,mango,uvas"
resultado = texto.split(",", 2)
print(resultado)  # Salida: ['manzana', 'pera', 'mango,uvas']


# Explicación:

# split(",", 2) divide el texto usando la coma (,) como separador.
# Realiza como máximo 2 divisiones, dejando el resto de la cadena intacto.
# Si no se especifica un separador:

texto = "   manzana   pera mango   "
resultado = texto.split()
print(resultado)  # Salida: ['manzana', 'pera', 'mango']
# Los espacios en blanco consecutivos se eliminan, y se obtiene solo las palabras. 😊

# --------------------------------------------------------------------------------------------




texto = "Hola\nMundo\rPython\r\n¡Aprende!"
resultado = texto.splitlines()
print(resultado)
# Salida:

# ['Hola', 'Mundo', 'Python', '¡Aprende!']
# Si activamos keepends=True para incluir los caracteres de salto de línea:

resultado_con_saltos = texto.splitlines(keepends=True)
print(resultado_con_saltos)
# Salida:

# ['Hola\n', 'Mundo\r', 'Python\r\n', '¡Aprende!']
# 😊


# ------------------------------------------------------------------------------------


texto = "Hola, mundo"

# ¿Empieza con "Hola"?
print(texto.startswith("Hola"))  # True

# ¿Empieza con "mundo"?
print(texto.startswith("mundo"))  # False

# ¿Empieza con "mundo" desde la posición 6?
print(texto.startswith("mundo", 6))  # True
# Salida:

# True
# False
# True


# ------------------------------------------------------------------------------------





# Ejemplo 1: Quitar espacios en blanco al principio y al final
texto = "   Hola, mundo   "
resultado = texto.strip()
print(resultado)
# Salida:

# "Hola, mundo"
# Ejemplo 2: Quitar caracteres específicos
url = "www.example.com"
resultado = url.strip("cmowz.")
print(resultado) # Salida: "example"
# Salida:

# "example"
# Aquí, Python quita cualquier combinación de los caracteres 'c', 'm', 'o', 'w', 'z', '.' al principio y al final de la cadena.

# Ejemplo 3: Limpiar una cadena con múltiples caracteres
comentario = "#....... Section 3.2.1 Issue #32 ......."
resultado = comentario.strip(".#! ")
print(resultado)  # Salida: "Section 3.2.1 Issue #32"
# Salida:

# "Section 3.2.1 Issue #32"
# Python elimina los caracteres '.', '#', '!', y espacio tanto al inicio como al final, hasta encontrar algo diferente. 😊

# -------------------------------------------------------------------------------------



texto = "Hola MUNDO"
resultado = texto.swapcase()
print(resultado)
# Salida:

# "hOLA mundo"
# Convierte las mayúsculas en minúsculas y las minúsculas en mayúsculas. 😊




# -------------------------------------------------------------------------------------




texto = "hola mundo desde python"
resultado = texto.title()
print(resultado)
# Salida:

# "Hola Mundo Desde Python"
# Convierte la primera letra de cada palabra a mayúscula. 😊


# -------------------------------------------------------------------------------------


# Crear un mapa de traducción
tabla = str.maketrans("aeiou", "12345")

# Aplicar la traducción
texto = "hola mundo"
resultado = texto.translate(tabla)
print(resultado)
# Salida:

# "h4l1 m5nd4"
# Aquí, las vocales 'a', 'e', 'i', 'o', 'u' son reemplazadas por '1', '2', '3', '4', '5' respectivamente. 😊


# -------------------------------------------------------------------------------------



texto = "Hola Mundo"
resultado = texto.upper()
print(resultado)
# Salida:

# "HOLA MUNDO"
# Este método convierte todos los caracteres que tienen versión en mayúscula a su forma mayúscula. 😊



# -------------------------------------------------------------------------------------



numero = "123"
resultado = numero.zfill(6)
print(resultado)
# Salida:

# "000123"
# Se rellenan ceros a la izquierda hasta que la longitud sea 6. 😊
























