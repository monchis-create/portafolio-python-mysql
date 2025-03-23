# El resultado de ingresar con la fucion input, siempre va hacer un string , asi que tengo que realizar un artificio que  se llama casting esto significa que tenemos que cambiar el tipo de dato entonces ahora queremos que ahora sea un tipo de dato integer en edad.

nombre = input("Ingrese su nombre: ")
print(nombre)
print(type(nombre))
edad = float(input("Ingrese su edad : "))
print(edad)
print(type(edad))

