a = 10
b = 3

print("suma:" , a + b)
print("resta:" , a - b)
print("multiplicacion:" , a * b)
print("potenciacion:" , a ** b)
print("division:" , a / b)
print("parte entera de la division:" , a // b)
print("Modulo:" , a % b)    # el modulo es el residuo de la division

a = a + 2
print( a ) #pero esto tambien se puede escribir asi , mira la siguiente linea de codigo

a += 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)


# PEMDAS explicado correctamente:
# P: Paréntesis – Resuelve primero lo que está dentro de paréntesis.
# E: Exponentes – Incluye potencias y raíces.
# MD: Multiplicación y División – Se resuelven de izquierda a derecha, según el orden en el que aparezcan.
# AS: Adición y Sustracción – También de izquierda a derecha, según el orden en el que aparezcan.




# cuando realizamos ejercicios matematicos mas complejos tenemos que seguir la norma pemdas osea primero la potenciacion , luego la exponenciacion, luego la matematica , luego la division , luego la adicion y la sustracion



# POTENCIACION
# EXPONENCIACION
# MULTIPLICACION O MATEMATICA
# DIVISION
# ADICION O SUMA
# SUSTRACION O RESTA


operation_1 = 2 + 3 * 4
print(operation_1)
operation_2 = 2 + (3 * 4)
print(operation_2)
operation_3 = (2 + 3) * (4**2)/8 - 1 # resulado es : 9
print(operation_3)




a = 10
b = 3 

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)