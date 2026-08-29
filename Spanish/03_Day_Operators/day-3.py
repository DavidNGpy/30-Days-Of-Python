# Operaciones aritméticas en Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # La división en python da un número flotante
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # da sin el número flotante o sin el resto
print('Modulus: ', 3 % 2)                           # Da el resto
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # significa 3 * 3

# Números Floating 
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Números Complex
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declarar la variable en la parte superior primero

a = 3 # a es un nombre de variable y 3 es un tipo de dato entero
b = 2 # b es un nombre de variable y 3 es un tipo de dato entero

# Operaciones aritméticas y asignación del resultado a una variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Debería haber usado sum en lugar de total, pero sum es una función integrada. Trate de evitar anular las funciones integradas.
print(total) # si no etiqueta su impresión con alguna cadena, nunca sabrá de dónde viene el resultado
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declarar valores y organizarlos juntos
num_one = 3
num_two = 4

# Operaciones aritmeticas
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Imprimiendo valores con etiqueta
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Cálculo del área de un círculo
radius = 10                                 # radio de un circulo
area_of_circle = 3.14 * radius ** 2         # dos * signo significa exponente o potencia
print('Area of a circle:', area_of_circle)

# Calcular el área de un rectángulo
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calcular el peso de un objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, porque 3 es mayor que 2
print(3 >= 2)    # True, porque 3 es mayor que 2
print(3 < 2)     # False,  porque 3 es mayor que 2
print(2 < 3)     # True, porque 2 es menor que 3
print(2 <= 3)    # True, porque 2 es menor que 3
print(3 == 2)    # False, porque 3 no es igual a 2
print(3 != 2)    # True, porque 3 no es igual a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparación booleana
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Comparación de otra forma
print('1 is 1', 1 is 1)                   # True - porque los valores de los datos son los mismos
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A encontrado en la cadena
print('B in Asabeneh', 'B' in 'Asabeneh') # False - no hay b mayúscula
print('coding' in 'coding for all') # True - porque codificar para todos tiene la palabra codificar
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - porque ambas afirmaciones son verdaderas
print(3 > 2 and 4 < 3) # False - porque la segunda afirmación es falsa
print(3 < 2 and 4 < 3) # False - porque ambas afirmaciones son falsas
print(3 > 2 or 4 > 3)  # True - porque ambas afirmaciones son verdaderas
print(3 > 2 or 4 < 3)  # True - porque uno de los enunciados es verdadero
print(3 < 2 or 4 < 3)  # False - porque ambas afirmaciones son falsas
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, entonces not verdadero da falso
print(not True)      # False - Negación, el operador not devuelve verdadero a falso
print(not False)     # True
print(not not True)  # True
print(not not False) # False

## 💻 Ejercicios - Día 3
'''''
1. Declara tu edad como variable entera
2. Declara tu altura como una variable flotante
3. Declarar una variable que almacene un número complejo
4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo (área = 0,5 x b x h).

py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100'''
edad=18
altura=1.70
num_complejo=3+4j

usuario=input("Ingrese la base del triángulo: ")
usuario_altura=input("Ingrese la altura del triángulo: ")
area=0.5*float(usuario)*float(usuario_altura)
print(f"El área del triángulo es: {area}")

'''5. Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo.
 Calcula el perímetro del triángulo (perímetro = a + b + c).

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
'''
lado_a=input("Ingrese el lado a del triángulo: ")
lado_b=input("Ingrese el lado b del triángulo: ")
lado_c=input("Ingrese el lado c del triángulo: ")
perimetro=float(lado_a)+float(lado_b)+float(lado_c)
print(f"El perímetro del triángulo es: {perimetro}")

'''6. Obtenga la longitud y el ancho de un rectángulo usando el indicador. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
7. Obtenga el radio de un círculo usando el aviso. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
8. Calcular la pendiente, la intersección x y la intersección y de y = 2x -2
9. La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la [distancia euclidiana](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) entre el punto (2, 2) y el punto (6,10)
10. Compara las pendientes en las tareas 8 y 9.
11. Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor de x y será 0.
12. Encuentra la longitud de 'python' y 'dragon' y haz una declaración de comparación falsa.
13. Use el operador _and_ para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
14. _Espero que este curso no esté lleno de jerga_. Use el operador _in_ para verificar si _jerga_ está en la oración.
15. No hay 'on' ni en dragón ni en pitón
16. Encuentre la longitud del texto _python_ y convierta el valor en flotante y conviértalo en cadena
17. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
18. Verifique si la división de piso de 7 por 3 es igual al valor int convertido de 2.7.
19. Comprueba si el tipo de '10' es igual al tipo de 10
20. Comprueba si int('9.8') es igual a 10
21. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?
'''
'''py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
'''
usuario_longitud=input("Ingrese la longitud del rectangulo: ")
usuario_ancho=input("Ingrese el ancho del rectangulo: ")
area_rectangulo=float(usuario_longitud)*float(usuario_ancho)
perimetro_rectangulo=2*(float(usuario_longitud)+float(usuario_ancho))
print(f"El área del rectángulo es: {area_rectangulo}")
print(f"El perímetro del rectángulo es: {perimetro_rectangulo}")


usuario_radio=input("Ingrese el radio del círculo: ")
area_circulo=3.14*float(usuario_radio)**2
circunferencia=2*3.14*float(usuario_radio)
print(f"El área del círculo es: {area_circulo}")
print(f"La circunferencia del círculo es: {circunferencia}")

pendiente=(10-2)/(6-2)
print(f"La pendiente es: {pendiente}")
interseccion_x=6-(10/pendiente)
interseccion_y=2-(pendiente*2)
print(f"La intersección con el eje x es: {interseccion_x}")
print(f"La intersección con el eje y es: {interseccion_y}")

y2=10
y1=2
x2=6
x1=2
pendiente=y2-y1/x2-x1
distancia_euclidiana=((6-2)**2+(10-2)**2)**0.5
print(f"La distancia euclidiana es: {distancia_euclidiana}")


print(f"La comparación de pendientes es: {pendiente==(10-2)/(6-2)}")

x=3
y=x**2 + 6*x + 9
print(f"El valor de y es: {y}")

p1='python'
p2='dragon'
print(len(p1)!=len(p2))

print('on' in p1 and 'on' in p2)

texto="_python_"

len_texto=float(len(texto))
len_texto_str=str(len_texto)


p1a="pitón"
p2a="dragón"
print('on' not in p1a and 'on' not in p2a)

palabra="espero que este curso no esté lleno de jerga"
print('jerga' in palabra)

numero=int(input("Ingrese un número: "))
print(f"El número {numero} es par: {numero%2==0}")
print(f"el numero{numero} NO es par: {numero%2!=0}")

print(f"La división de piso de 7 por 3 es igual a int(2.7): {7//3==int(2.7)}")

print(f"El tipo de '10' es igual al tipo de 10: {type('10')==type(10)}")

print(f"int('9.8') es igual a 10: {int(float('9.8'))==10}")

horas=int(input("Ingrese las horas trabajadas: "))
tarifa=float(input("Ingrese la tarifa por hora: "))

paga=horas*tarifa
print(f"Su salario semanal es: {paga}")

#22. Escriba un script que le solicite al usuario que ingrese el número de años. Calcula el número de segundos que una persona puede vivir. Suponga que una persona puede vivir cien años.

'''py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
'''
años=int(input("Ingrese el número de años que ha vivido: "))
segundos=años*365*24*60*60
print(f"Has vivido por {segundos} segundos.")

'''23. Escriba un script de Python que muestre la siguiente tabla

py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
''' 


print(f"{1**1} {1**0} {1**1} {1**2} {1**3}")
print(f"{2**2} {2**0} {2**1} {2**2} {2**3}")
print(f"{3**3} {3**0} {3**1} {3**2} {3**3}")
print(f"{4**4} {4**0} {4**1} {4**2} {4**3}")
print(f"{5**5} {5**0} {5**1} {5**2} {5**3}")
