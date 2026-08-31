## 💻 Ejercicios - Día 5

### Ejercicios: Nivel 1

#1. Declara una lista vacía
lista_vacia= list()
#2. Declara una lista con más de 5 elementos
lista_5=["1",2,"tres",True,False]

#3. Encuentra la longitud de la lista
lst=['x','y','z']

len_lista=len(lst)

#4. Obtén el primer, medio y último elemento de la lista
lista=["1","2","3"]
lista_prel= lista[0]
lista_m=lista[1]
last_element= lista=[2]

#5. Declara una lista llamada `mixed_data_types` que contenga tu nombre, edad, altura, estado civil y dirección

mixed_data_types=["David", 18, 1.70, "Soltero","xd"]

#6. Declara una lista `it_companies` e inicialízala con: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
#7. Imprime la lista usando `print()`
print(it_companies)
#8. Imprime el número de empresas en la lista
print(f"numero de empresas: {len(it_companies)}")

#9. Imprime la primera, la del medio y la última empresa
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])


#10. Cambia el nombre de una de las empresas y vuelve a imprimir la lista
it_companies[0]="Tesla"

print(it_companies)

#11. Agrega una empresa IT a `it_companies`
it_companies.append("IBM")

#12. Inserta una empresa IT en la mitad de la lista

it_companies.insert(3,"DeepSeek")

#13. Cambia el nombre de una empresa en `it_companies` a mayúsculas (¡excepto IBM!)
it_companies[0]= it_companies[0].upper()

#14. Une `it_companies` en una cadena usando la cadena '#;&nbsp; '
resultado = '#;&nbsp; '.join(it_companies)

#15. Verifica si una empresa existe en `it_companies`
existe= "IBM" in it_companies
print(existe)
#16. Ordena la lista usando el método `sort()`
listanum=[5,3,2,4,1]
ord=listanum.sort()
print(ord)
#17. Invierte la lista en orden descendente usando `reverse()`
listaaa=listanum.reverse()
print(listaaa)


#18. Corta (slice) las primeras 3 empresas de la lista
primeras_3_empresas = it_companies[:3]
print(primeras_3_empresas)

#19. Corta (slice) las últimas 3 empresas de la lista
ultimas_3_empresas= it_companies[-3:]
print(ultimas_3_empresas)
#20. Corta la(s) empresa(s) del medio de la lista
medio_empresas= it_companies[4:5]
print(medio_empresas)
#21. Elimina la primera empresa IT de la lista


del it_companies[0] 

#22. Elimina la(s) empresa(s) del medio de la lista
del it_companies [4:5]
#23. Elimina la última empresa IT de la lista
del it_companies[-1]
#24. Elimina todas las empresas IT de la lista
del it_companies[0:8]
#25. Destruye la lista `it_companies`
del it_companies

#26. Concatena las siguientes listas:

#    ```py
 #   front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
  #  back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullstack=front_end + back_end
print(fullstack)
    
#27. Inserta 'Python' y 'SQL' después de `full_stack` en la lista concatenada.
lenguajes=['Pyhon','SQL']
fullstak_lenguajes= fullstack + lenguajes
### Ejercicios: Nivel 2

#1. A continuación, una lista con las edades de 10 estudiantes:

##```py
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#```
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#- Ordena la lista y encuentra la edad máxima y mínima
list_ordenada=ages.sort()
lista_max=ages.max()
lista_min=ages.min()

##- Agrega la edad mínima y máxima nuevamente a la lista
list_ordenada.append(lista_max)
list_ordenada.append(lista_min)

#- Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios)
ages_sort=sorted(ages)
mitad=len(ages_sort)//2
mediana=(ages_sort[mitad-1]+ ages_sort)

#- Encuentra la edad promedio (suma de todos los elementos dividida por su cantidad)
media=sum(ages)/len(ages)
#- Encuentra el rango de edades (máximo - mínimo)
rango=lista_max-lista_min

#- Compara |min - promedio| y |max - promedio| usando la función `abs()`
diferencia_min = abs(lista_min - media)
diferencia_max = abs(lista_max - media)


#1. Encuentra el país del medio en la [lista de países](https://github.com/Taki-Ta/30-Days-Of-Python-Simplified_Chinese_Version/tree/master/data/countries.py)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

middle_index = len(countries) // 2
print(countries[middle_index])


#2. Divide la lista de países en dos listas iguales (si es par; si no, la primera lista tendrá un país más)
corte = (len(countries) + 1) // 2

primera_mitad = countries[:corte]
segunda_mitad = countries[corte:]
print(len(primera_mitad)) 
print(len(segunda_mitad))

#3. Para la lista ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'], separa los tres primeros países de los países nórdicos restantes.
paises=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
pais1,pais2,pais3,*nordicos = paises