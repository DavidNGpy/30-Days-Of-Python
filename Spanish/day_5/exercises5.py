## 💻 Ejercicios - Día 5

### Ejercicios: Nivel 1
"""
1. Declara una lista vacía
lista_vacia= List()
2. Declara una lista con más de 5 elementos
lista_5=["1",2,"tres",True,False]

3. Encuentra la longitud de la lista
lst=[x,y,z]

len_lista=len(lista)

4. Obtén el primer, medio y último elemento de la lista
lista=["1","2","3"]
lista_prel= lista[0]
lista_m=lista[1]
last_element= lista=[2]

5. Declara una lista llamada `mixed_data_types` que contenga tu nombre, edad, altura, estado civil y dirección

mixed_data_types=["David", 18, 1.70, "Soltero","xd"]

6. Declara una lista `it_companies` e inicialízala con: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
7. Imprime la lista usando `print()`
print(it_companies)
8. Imprime el número de empresas en la lista
print(f"numero de empresas: {len(it_companies)}")

#9. Imprime la primera, la del medio y la última empresa
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])


#10. Cambia el nombre de una de las empresas y vuelve a imprimir la lista
it_companies[0]="Tesla"

print(it_companies)

11. Agrega una empresa IT a `it_companies`
it_companies.append("IBM")

12. Inserta una empresa IT en la mitad de la lista

it_companies.insert(3,"DeepSeek")

13. Cambia el nombre de una empresa en `it_companies` a mayúsculas (¡excepto IBM!)
frutas[0]= frutas[0].upper()

14. Une `it_companies` en una cadena usando la cadena '#;&nbsp; '
resultado = '#;&nbsp; '.join(it_companies)

15. Verifica si una empresa existe en `it_companies`
existe= "IBM" in it_companies
print(existe)
16. Ordena la lista usando el método `sort()`
listanum=[5,3,2,4,1]
ord=listanum.sort()
print(ord)
17. Invierte la lista en orden descendente usando `reverse()`

18. Corta (slice) las primeras 3 empresas de la lista
19. Corta (slice) las últimas 3 empresas de la lista
20. Corta la(s) empresa(s) del medio de la lista
21. Elimina la primera empresa IT de la lista
22. Elimina la(s) empresa(s) del medio de la lista
23. Elimina la última empresa IT de la lista
24. Elimina todas las empresas IT de la lista
25. Destruye la lista `it_companies`
26. Concatena las siguientes listas:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    
27. Inserta 'Python' y 'SQL' después de `full_stack` en la lista concatenada.

### Ejercicios: Nivel 2

1. A continuación, una lista con las edades de 10 estudiantes:

```py
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Ordena la lista y encuentra la edad máxima y mínima
- Agrega la edad mínima y máxima nuevamente a la lista
- Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios)
- Encuentra la edad promedio (suma de todos los elementos dividida por su cantidad)
- Encuentra el rango de edades (máximo - mínimo)
- Compara |min - promedio| y |max - promedio| usando la función `abs()`

1. Encuentra el país del medio en la [lista de países](https://github.com/Taki-Ta/30-Days-Of-Python-Simplified_Chinese_Version/tree/master/data/countries.py)
2. Divide la lista de países en dos listas iguales (si es par; si no, la primera lista tendrá un país más)
3. Para la lista ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'], separa los tres primeros países de los países nórdicos restantes.
"""