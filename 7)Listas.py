to_do = [
    "Dirigirnos al hotel",
    "Ir a almozar" ,
    "visitar un museo",
    "Volver al hotel"
]
print(to_do)

numbers = [1,2,3,4, "cinco"]
print(numbers)





mix = ["uno" , 2, 3.14 , True , [1,2,3]]
print(mix)
print(len(mix)) #Len es par ver la logitud de mi cadena en este caso la cadena mix.(5)


print("Primer elemento" , mix[0]) # uno
print("Segundo elemento" , mix[1]) # 2 

# Tanto el menos uno como el cuatro dan el mismo resultado
print("Ultimo elemento" , mix[4]) # [1,2,3]
print("Ultimo elemento" , mix[-1])# [1,2,3]



string = "Hola mundo"
print("Primer elemento" , string[0]) # H
print("Segundo elemento" , string[1]) # o

# Tanto el menos uno como el nueve dan el mismo resultado
print("Ultimo elemento" , string[9]) # o
print("Ultimo elemento" , string[-1]) # o


print(mix[0:2]) # [uno,2]
# es una buena practica dejarlo vacio y no ponerlo en la posicion cero
print(mix[:2]) # [uno,2]

print(mix[2:]) # [3.14, True , [1,2,3]]
print(mix[2:-2]) # [3.14]


print(mix) # ['uno', 2, 3.14, True, [1, 2, 3]]
mix.append(False)
print(mix) # ['uno', 2, 3.14, True, [1, 2, 3], False]


mix.append(["a","b"])
print(mix) # ['uno', 2, 3.14, True, [1, 2, 3], False, ['a', 'b']]


mix.insert(1,["a","b"])
print(mix) #['uno', ['a', 'b'], 2, 3.14, True, [1, 2, 3], False, ['a', 'b']] , inserta a y b a la posicion uno

print(mix.index(["a","b"])) # index me muestra la primera aparicion de esta con un numero uno: 1
# El método index en Python busca un elemento en una lista y devuelve la posición (índice) en la que aparece por primera vez.

posicion = mix.index(["a","b"])
print("El número 2 está en la posición:", posicion)



numbers = [1,2,100.01, 90.45 , 3,4,5]
print("Mayor:", max(numbers)) # Mayor: 100.01
print("Menor:", min(numbers)) # Menor: 1

# minuto 12:16


# Por ultimo puedo eliminar elementos de la lista , inclusive la lista entera

# Del numbers quiero eliminar la posicion menos uno
del numbers[-1] # [1, 2, 100.01, 90.45, 3, 4]
print(numbers)

# elimina la posicion 0 y 1
del numbers[:2] # [100.01, 90.45, 3, 4]
print(numbers)

# Cuando intentamos hacer un print osea a imprimir la informacion que est ahi, nos aparece un error porque en ese momento del codigo ya no existe esa lista
#del numbers
#print(numbers)

























mix = ["uno", 2, "tres", 4, "cinco" ]
print(mix)
print(len(mix))
print(mix[0])

print(mix[4][2])
print(mix[4][-2])
print(mix[4][1:4])

mix.extend(["nueve",8])
print(mix)
mix.remove("nueve") 
print(mix)