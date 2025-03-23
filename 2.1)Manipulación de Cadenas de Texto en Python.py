# Ejemplo con la letra especial alemana 'ß'
texto = "straße"

# Usando lower()
texto_lower = texto.lower()
print("Con lower():", texto_lower)  # Salida: "straße" (no cambia)

# Usando casefold()
texto_casefold = texto.casefold()
print("Con casefold():", texto_casefold)  # Salida: "strasse" (cambia 'ß' a "ss")


# ------------------------------------------------------------------------


# Cadena de texto a centrar
texto = "Hola"

# Centrar el texto en una longitud de 10, usando espacios por defecto
texto_centrado = texto.center(10)
print("Con espacios:", repr(texto_centrado))  # Salida: '   Hola   '

# Centrar el texto en una longitud de 10, usando un carácter de relleno personalizado
texto_centrado_con_asteriscos = texto.center(10, "*")
print("Con asteriscos:", repr(texto_centrado_con_asteriscos))  # Salida: '***Hola***'




# --------------------------------------------------------------------------------------------




# Tenemos una palabra
palabra = "manzana"

# Queremos contar cuántas veces aparece la letra "a"
cuenta_a = palabra.count("a")

# Mostramos el resultado
print("La letra 'a' aparece", cuenta_a, "veces en la palabra.") # Esto mostrará: La letra 'a' aparece 3 veces en la palabra.




# --------------------------------------------------------------------------------------------





# Nuestro texto original
texto = "Hola, ¿cómo estás?"

# Convertimos el texto a bytes usando la codificación utf-8
texto_bytes = texto.encode('utf-8')

# Mostramos el resultado en bytes
print(texto_bytes)  

# salida :  b'Hola, \xc2\xbfc\xc3\xb3mo est\xc3\xa1s?'





text = b'mundo hol\xc3\x9fa'
decoded_text = text.decode('utf-8')
print(decoded_text) # Salida: mundo holá







# --------------------------------------------------------------------------------------------



# Ejemplo básico: verificar si la cadena termina con "mundo"
s = "hola mundo"
resultado = s.endswith("mundo")
print(resultado)  # Salida: True    

# Ejemplo con inicio y fin: verificar si "hola mundo" termina con "la" desde la posición 0 hasta 4
resultado = s.endswith("la", 0, 4)
print(resultado)  # Salida: True (porque "hola" termina en "la")

# Ejemplo con tupla de sufijos
resultado = s.endswith(("mundo", "planeta"))
print(resultado)  # Salida: True (porque "mundo" es uno de los sufijos)







# Aquí está nuestra frase
frase = "Hola, mundo!"

# Queremos ver si la frase termina en "mundo!"
termina_en_mundo = frase.endswith("mundo!")

# Mostramos el resultado
print(termina_en_mundo)  # Esto mostrará: True






# También podemos ver si la frase termina en varias palabras posibles, como "mundo!" o "adiós!":
termina_en_algo = frase.endswith(("mundo!", "adiós!"))
print(termina_en_algo)  # Esto mostrará: True    ,   (porque "mundo!" es uno de los sufijos)





# -----------------------------------------------------------------------------------





# Texto con tabuladores (\t) que queremos expandir a espacios
texto = "Perro\tGato\tConejo\tHamster"

# Expande los tabuladores a espacios (con un tamaño de 8 por defecto)
texto_expandido = texto.expandtabs(19)

print("Texto original con tabuladores:")
print(texto)    # Salida: Perro   Gato    Conejo  Hamster
print("Texto con los tabuladores convertidos en espacios:")
print(texto_expandido) # Salida: Perro               Gato                Conejo              Hamster



# --------------------------------------------------------------------------------------------


# 'h' está en la posición 0
# 'o' está en la posición 1
# 'l' está en la posición 2
# 'a' está en la posición 3




s = "hola"
sub = "o"

# Usando find para obtener la posición
posicion = s.find(sub)
print(posicion)  # Salida: 1 (porque 'o' está en la posición 1)

# Usando in para comprobar si "o" está en "hola"
existe = sub in s
print(existe)  # Salida: True




# --------------------------------------------------------------------------------------------

name = "Carlos"
age = 25

# Usamos las llaves {} para reemplazar con variables.
sentence = "Hola, mi nombre es {} y tengo {} años.".format(name, age)

print(sentence)

# Hola, mi nombre es Carlos y tengo 25 años.




sentence = "El número {0} es menor que el número {1}".format(5, 10)
print(sentence) # Salida: El número 5 es menor que el número 10




# -------------------------------------------------------------------------------------------







# Aquí, format_map toma los valores del diccionario datos y los inserta en los marcadores {nombre} y {edad} dentro de mensaje. Pero no guarda nada


mensaje = "Hola, mi nombre es {nombre} y tengo {edad} años."
datos = {'nombre': 'Juan', 'edad': 10}
resultado = mensaje.format_map(datos)
print(resultado)
