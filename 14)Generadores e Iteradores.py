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