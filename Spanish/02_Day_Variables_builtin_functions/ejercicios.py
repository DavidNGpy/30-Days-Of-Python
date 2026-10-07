'''Ejercicios: Nivel 1
Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py
Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
Declarar una variable de nombre y asignarle un valor
Declarar una variable de apellido y asignarle un valor
Declare una variable de nombre completo y asígnele un valor
Declarar una variable de país y asignarle un valor
Declarar una variable de ciudad y asignarle un valor
Declarar una variable de edad y asignarle un valor
Declarar una variable de año y asignarle un valor
Declarar una variable is_married y asignarle un valor
Declarar una variable is_true y asignarle un valor
Declare una variable is_light_on y asígnele un valor
Declarar múltiples variables en una línea'''

print("Día 2: 30 días de programación en python")
nombre = " David"
apellido = " nieto"
nombre_completo = nombre + apellido
pais = " México"
ciudad = " Ciudad de México"
edad = 30
año = 1997
is_married = False
is_true = True
is_light_on = False
variable1, variable2, variable3 = "valor1", "valor2", "valor3"

'''Ejercicios: Nivel 2
Verifique el tipo de datos de todas sus variables usando la función incorporada type()

Usando la función incorporada len(), encuentre la longitud de su nombre
Compara la longitud de tu nombre y tu apellido
Declarar 5 como num_one y 4 como num_two
Sume num_one y num_two y asigne el valor a un total variable
Reste num_two de num_one y asigne el valor a una variable diff
Multiplique num_two y num_one y asigne el valor a un producto variable
Divide num_one por num_two y asigna el valor a una división variable
Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un residuo variable
Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division
El radio de un círculo es de 30 metros.
Calcule el área de un círculo y asigne el valor a una variable con el nombre de area_of_circle
Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
Tome el radio como entrada del usuario y calcule el área.
Use la función de entrada integrada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras o palabras clave reservadas de Python'''

print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

len_nombre= len(nombre)
len_apellido= len(apellido)
comparacion_longitud = len_nombre == len_apellido
numero_uno = 5
numero_dos = 4
sumar= numero_uno + numero_dos
restar= numero_uno - numero_dos
multiplicar_producto_variable= numero_uno * numero_dos
dividir= numero_uno / numero_dos

residuo= numero_uno % numero_dos

potencia= numero_uno ** numero_dos
div_floor= numero_uno // numero_dos

r=30
area=3.14 * r ** 2
circunferencia= 2 * 3.14 * r

nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
pais_usuario = input("Ingrese su país: ")
edad_usuario = input("Ingrese su edad: ")