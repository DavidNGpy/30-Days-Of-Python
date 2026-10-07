#1. Une las cadenas 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'.
strings_unidas=" ".join(['Thirty', 'Days', 'Of', 'Python'])
#2. Une las cadenas 'Coding', 'For', 'All' en 'Coding For All'.
strings_unidas2=" ".join(['Coding', 'For', 'All'])
#3. Declara la variable `company` y asígnale el valor inicial "Coding For All".
str="Coding For All"
#4. Imprime la variable `company` usando `print()`.
print(str)
#5. Usa `len()` y `print()` para mostrar la longitud de la cadena `company`.
print(len(str))
#6. Usa el método `upper()` para convertir todos los caracteres a mayúsculas.
print(str.upper())
#7. Usa el método `lower()` para convertir todos los caracteres a minúsculas.
print(str.lower())
#8. Aplica `capitalize()`, `title()` y `swapcase()` sobre la cadena 'Coding For All'.
print(str.capitalize())
print(str.title())
print(str.swapcase())
#9. Extrae mediante slicing la primera palabra de 'Coding For All'.
print(str[0:6])
#10. Usa `index`, `find` u otros métodos para comprobar si la cadena 'Coding For All' contiene la palabra 'Coding'.
print(str.index('Coding'))
#11. Reemplaza la palabra 'Coding' por 'Python' en 'Coding For All'.
print(str.replace('Coding', 'Python'))
#12. Reemplaza 'Python for Everyone' por 'Python for All' (usa `replace()` u otro método).
print('Python for Everyone'.replace('Everyone', 'All'))
#13. Separa la cadena 'Coding For All' usando espacios como separador.
print(str.split())
#14. Divide la cadena 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' por las comas.
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))
#15. ¿Qué carácter está en el índice 0 de 'Coding For All'?
str='Coding For All'
print(str[0])
#16. ¿Cuál es el índice del último carácter de 'Coding For All'?
print(str[-1])

#17. ¿Qué carácter está en el índice 10 de 'Coding For All'?
print(str[10])

#18. Crea una sigla (acrónimo) a partir de 'Python For Everyone'.
strp='Python For Everyone'
print(strp[0]+strp[7]+strp[11])

#19. Crea una sigla a partir de 'Coding For All'.
print(str[0]+str[7]+str[11])
#20. Usando `index`, determina la primera aparición de la letra 'C' en 'Coding For All'.
print(str.index('C'))
#21. Usando `index`, determina la primera aparición de la letra 'F' en 'Coding For All'.
print(str.index('F'))
#22. Usa `rfind` para determinar la última aparición de 'l' en 'Coding For All People'.
print(str.rfind('l'))
#23. Usa `index` o `find` para encontrar la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.index('because'))
#25. Elimina la frase 'because because because' de: 'You cannot end a sentence with because because because is a conjunction'.
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.replace('because because because', ''))
#27. Elimina la frase 'because because because' de la oración anterior.
print(frase.replace('because because because', ''))
#28. ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?
print(str.startswith('Coding'))
#29. ¿La cadena 'Coding For All' termina con la subcadena 'coding'?
print(str.endswith('coding'))
#30. Elimina los espacios en blanco a la izquierda y derecha de la cadena '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'.
text = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
print(text.replace('&nbsp;', '').strip())
#31. Usando `isidentifier()`, ¿cuál de las siguientes devuelve `True`?
 #   - 30DaysOfPython
  #  - thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#32. Dada la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'], únela en una cadena separada por espacios.
lista=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(lista))
#33. Usa la secuencia de escape de nueva línea para separar las siguientes oraciones:
 #   ```py
  #  I am enjoying this challenge.
   # I just wonder what is next.
    #```

print("I am enjoying this challenge.\nI just wonder what is next."
      )
#34. Usa la secuencia de tabulación para mostrar:
   # ```py
   # Name      Age     Country   City
   # Asabeneh  250     Finland   Helsinki
   # ```
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#35. Usa un método de formateo de cadenas para imprimir:

#```py
radius = 10
area = 3.14 * radius ** 2
print(f"El área de un círculo con radio {radius} es {area} metros cuadrados.")
# The area of a circle with radius 10 is 314 meters square.
#```
print(f"El área de un círculo con radio {radius} es {area} metros cuadrados.")

#36. Usa un método de formateo de cadenas para imprimir:

#```py
'''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''
print(f"8 + 6 = {8 + 6}\n8 - 6 = {8 - 6}\n8 * 6 = {8 * 6}\n8 / 6 = {8 / 6:.2f}\n8 % 6 = {8 % 6}\n8 // 6 = {8 // 6}\n8 ** 6 = {8 ** 6}")