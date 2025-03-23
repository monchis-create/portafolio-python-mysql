# Lectura de funciones y metodos de python :  https://docs.python.org/es/3/library/stdtypes.html#string-methods
# Lectura de funciones y metodos de python :  https://docs.python.org/es/3/library/stdtypes.html#string-methods
# Lectura de funciones y metodos de python :  https://docs.python.org/es/3/library/stdtypes.html#string-methods
# Lectura de funciones y metodos de python :  https://docs.python.org/es/3/library/stdtypes.html#string-methods
# Lectura de funciones y metodos de python :  https://docs.python.org/es/3/library/stdtypes.html#string-methods


name = "carly"
print(type(name))

# Resultado : <class 'str'> , str quiere decir string.




# Las comillas triples no me va a marcar error vscode  puedo seguir escribiendo normalmente mientras que las comillas simples y dobles si me va a marcar un error.


name = '''carly

manuela
'''
print(name)


name = """carly

manuela
"""
print(name)







# --------------------------------------------------------------------------------------------

name = "Carla Marcela"
print(name[0])
print(name[1])
print(name[2])
print(name[-3])  #e , el -3 es la letra e                     



# --------------------------------------------------------------------------------------------



name = "CARLA Marcela"
last_name = "       Florida       Roman     "

# El resultado es que se repite cinco veces carla marcela
print(name * 5)  #CARLA MarcelaCARLA MarcelaCARLA MarcelaCARLA MarcelaCARLA Marcela

# Aqui se concatena name y last_name osea se une o se pega.
print(name + " " + last_name) #CARLA Marcela        Florida       Roman             


# Aqui cuenta la longitud de la o cuantas letras o espacios tiene un string, len

print(len(name)) #13
print(len(last_name)) #31


# Estos son metodos , las de arriba se llaman funciones.
# Esto transformas a minusculas las letras.
print(name.lower())

# Esto transforma a mayusculas las letras.
print(name.upper())

# Elimina los espacios que tiene de mas 
print(last_name.strip())



# --------------------------------------------------------------------------------------------




# Cadena en la que vamos a buscar
texto = "Hola, bienvenido a Python"

# Subcadena que buscamos
subcadena = "Python"

# Buscar la posición de la subcadena
try:
    posicion = texto.index(subcadena)
    print(f"La subcadena '{subcadena}' se encuentra en la posición {posicion}.")
except ValueError:
    print(f"La subcadena '{subcadena}' no se encontró en el texto.")


# --------------------------------------------------------------------------------------------




# osea str.capitalize() pone la primera letra en mayuscula sierto dejando la segunda letra en minuscula sierto
# ChatGPT Plus
# ¡Exacto! str.capitalize() toma solo la primera letra y la pone en mayúscula, mientras que todas las demás letras las deja en minúscula, sin importar cómo estaban antes.

# Por ejemplo:

# python
# Ejemplo con letras mezcladas
palabra = "gRANDE"
palabra_capitalizada = palabra.capitalize()
print(palabra_capitalizada)
# Resultado:

# Grande
# Aunque "gRANDE" tenía varias letras en mayúsculas y minúsculas, str.capitalize() solo puso la primera letra en mayúscula ("G") y cambió el resto a minúsculas.










