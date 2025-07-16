####   PROYECTO LÓGICA: Katas de Python   ####
"""
 1 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
de cada letra en la cadena. Los espacios no deben ser considerados.
"""
def CuentaLetras(texto):
    """Función para contar las letras que hay en un texto

    Args:
        texto (str): Texto del que queremos contar las letras

    Returns:
        dict : Devuelve un diccionario con las letras que aparecen en el texto y el número de apariciones de cada una
    """
    #definimos una variable diccionario vacía
    listado = {}

    for caracter in texto: #recorremos todo el texto introducido
        if caracter != ' ': # comprobamos si el caracter es distinto de ' '
            caracter = caracter.lower() #lo convertimos a minuscula 
            if caracter in listado:     
                listado[caracter] += 1  #si el caracter esta ya en nuestro diccionario lo incrementamos en 1
            else:
                listado[caracter] = 1   #si el caracter no está lo inicializamos a 1

    return listado

#PROBAMOS
miCadena = "abcadc"
print("Ejercicio 1")
print("Resultado: " + str(CuentaLetras(miCadena))) #{'a': 2, 'b': 1, 'c': 2, 'd': 1}
print(" ")
print(" ")

""" 
2 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
"""
#Definimos una función que pasando un valor nos devuelve el doble
def DuplicarValor(x):
    """Función que sirve para duplicar el valor de una variable

    Args:
        x (int): Valor numérico 

    Returns:
        int: Valor x2
    """
    return x*2
#Definimos nuestra lista de numeros  
miListaNumeros = [1,2,3,4,5,6]
##Usamos la función map para ejecutar nuestra función DuplicarValor en todos los elementos,
#el resultado lo convertimos en una lista y lo asignamos a nuestra nueva lista
nuevaListaNumeros = list(map(DuplicarValor,miListaNumeros))
#Imprimimos los resultados
print("Ejercicio 2")
print("Resultado: " + str(nuevaListaNumeros)) #[2, 4, 6, 8, 10, 12]
print(" ")
print(" ")


"""
3 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""
def BuscaPalabra(listaPalabras,strABuscar):
    """Función para buscar dentro de una lista de palabras aquellas que contienen una cadena de caracteres dada

    Args:
        listaPalabras (list): Lista de palabras en las que buscar
        strABuscar (str): caracteres que queremos encontrar

    Returns:
        list: Lista con las palabras que contienen la cadena de caracteres deseada
    """
    #Definimos una nueva lista de palabras vacía
    nuevaListaPalabras =[]
    for palabra in listaPalabras: #Recorremos todas las palabras de nuestra lista
        if palabra.find(strABuscar) != -1: 
            nuevaListaPalabras.append(palabra) #Si encontramos la cadena de caracteres en la palabra añadimos la palabra a nuestra nueva lista

    return nuevaListaPalabras #Devolvemos la nueva lista de palabras

#Definimos una lista de palabras
milistaPalabras = ["programa","programador","programación","teclado","ratón"]

print("Ejercicio 3")
print(f"     Mi lista de palabras es: {milistaPalabras}  y busco las que contengan ón")
print("     " + str(BuscaPalabra(milistaPalabras,"ón")))
print(" ")

"""
4 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""
#Definimos una función de restar valores
def RestarValores(x,y):
    """Función para restar dos valores dados

    Args:
        x (float): Numero 1
        y (float): Número a restar

    Returns:
        float: resultado de la resta x-y
    """
    return x-y

miListaNumeros1 = [2,5,7,2,99]  #Definimos nuestra nueva lista de numeros 1
miListaNumeros2 = [1,0,88,43,4] #Definimos nuestra nueva lista de numeros 2
#Obtenemos una resta de todos los componentes de las listas usando nuestra función
#y la devolvemos a una nueva lista
resultadoResta = list(map(RestarValores,miListaNumeros1,miListaNumeros2)) 
#Imprimimos resultado
print("Ejercicio 4")
print("Resultado: " + str(resultadoResta))
print(" ")
print(" ")


"""
5 Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado.
"""
def AnalizarNotas(listaNotas,aprobado=5):
    """Función que devuelve una tupla, con la nota media y la evaluación de si está o no aprobado_summary_

    Args:
        listaNotas (list): lista con las notas en float del alumno
        aprobado (float): Nota del aprobado, por defecto 5

    Returns:
        str: "aprobado" o "suspenso" en función de
    """
    
    #Cálculo de la nota media    
    notaMedia = sum(listaNotas)/len(listaNotas)
    if notaMedia >= aprobado:
        resultados = (notaMedia,"aprobado") #Nota mayor del aprobado
    else:
        resultados = (notaMedia,"suspenso") #Nota menor del aprobado
    
    return resultados

#Definimos nuestra lista de notas a analizar
notas = [5.6,7.8,6.3,4]
#Imprimimos resultado
print("Ejercicio 5")
print("Resultado: ")
print("       Las notas a evaluar son: " + str(notas))
print("       La nota media y el resultado final es: " + str(AnalizarNotas(notas,7)))
print(" ")
print(" ")


"""
6 Escribe una función que calcule el factorial de un número de manera recursiva.
""" 
def factorial(n):
    """Función que devuelve el cálculo del factorial de un número

    Args:
        n (int): número del que queremos calcular el factorial

    Returns:
        int: Valor con el factorial del número deseado
    """
    
    #A tener en cuenta: 
    #       el factorial de 0 = 1
    #       el factorial de un numero negativo no existe
    if n < 0:
        return -1
    else:
        if n == 0 or n == 1:
            return 1
        else:
            return n*factorial(n-1) #Usamos recursividad para ir calculando el factorial deseado

#Probamos        
miNumero = 5
print("Ejercicio 6")
print("Resultado: ")
print("       El factorial de: " + str(miNumero) + " es: " + str(factorial(miNumero)))
print(" ")
print(" ")



"""
7 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
"""
def ConvertirAStr(valor):
    return str(valor)

miListaTuplas = [("hola","adios"),("rojo","verde","ambar")]
miListaStr = list(map(ConvertirAStr,miListaTuplas))

#Probamos        
print("Ejercicio 7")
print("Resultado: ")
print("       Mi lista de tuplas en string es: " + str(miListaStr))
#Está generando una lista de elementos string con las tuplas en cada componente de la lista
print(" ")
print(" ")


"""
8 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no.
"""
def division():
    """Función que gestiona una división entre dos números que sesolicitan al usuario
    """
    #Gestionamos las excepciones con try
    try:
        dividendo = float(input("Introduzca un valor numérico: ")) #Pedimos el primer número
        divisor = float(input("Introduzca un valor numérico distinto de 0 como divisor: ")) #pedimos el segundo número
        resultado = dividendo/divisor #intentamos dividir
    except ValueError:  #Gestionamos la excepción de no tratarse de números
        print("Error: Los valores introducidos no son números")
    except ZeroDivisionError: #Gestionamos la excepción de dividir por 0
        print("Error: No se puede dividir por 0")
    else:   #En caso de ser correcto
        print(f"El resultado de la división es: {resultado}")

#Probamos        
print("Ejercicio 8")
print("Resultado: ")
print("       Mi prueba de division: " + str(division()))
print(" ")
print(" ")                        


"""
9 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
"""
def filtrar_mascotas_permitidas(lista_mascotas):
    """Función que filtra una lista de mascotas dada, excluyendo unas determinadas

    Args:
        lista_mascotas (list): lista de mascotas

    Returns:
        list: lista con la lista original quitando las mascotas que hay que excluir
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

mascotas = ["Perro", "Gato", "Mapache", "Serpiente Pitón", "Conejo"]
mascotas_permitidas = filtrar_mascotas_permitidas(mascotas)
#Probamos        
print("Ejercicio 9")
print("Resultado: ")
print(f"       La lista de mascotas permitidas son:  {mascotas_permitidas}")
print(" ")
print(" ")      
    

"""
10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
excepción personalizada y maneja el error adecuadamente.
"""
def valorMedio(listaNum):
    """Función que calcula el valor de medio de los números de una lista con control de excepciones

    Args:
        listaNum (list): Lista de números

    Returns:
        float: Valor medio de la lista
    """
    
    #Como hay que generar un control de excepciones hacemos uso del try
    try:
        promedio = sum(listaNum)/len(listaNum)
    except ValueError:  #Gestionamos la excepción de no tratarse de números
        print("Error: Los valores introducidos no son números")    
        promedio = 0
    except ZeroDivisionError: #Gestionamos la excepción de dividir por 0
        print("Error: La lista de números proporcionada está vacía")
        promedio = 0
    return promedio

#Definimos nuestra lista de números
miListaNumeros3 = [4,7,2,5,9,10,23]
mediaListaNumeros = valorMedio(miListaNumeros3)

print("Ejercicio 10")
print(f"    La lista de números es: {miListaNumeros3} ")
print(f"    El promedio de los números es:  {mediaListaNumeros}")
print(" ")
print(" ")     

"""
11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente.
"""
def PedirEdad():
    """Función que pide la edad al usuario y controla que esté entre 0 y 120 y que sea un número
    """
    try:
        edad = int(input("Introduzca su edad: ")) #Pedimos la edad del usuario
        if edad < 0 or edad > 120:
            print("Error: La edad está fuera de los rangos esperados")
        else:
            print(f"Le edad introducida es: {edad}")
    except ValueError:  #Gestionamos la excepción de no tratarse de números
        print("Error: El valor introducido no es un número")
    
#Probamos        
print("Ejercicio 11")
print("Resultado: ")
PedirEdad()
print(" ")
print(" ")                        

"""
 12 Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
"""
def HallarLongitudesPalabras(frase):
    """Función que devuelve una lista con la longitud de las palabras de una frase dada

    Args:
        frase (str): Frase que queremos analizar

    Returns:
        list: lista con las longitudes de todas las palabras
    """
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

#Probamos
print("Ejercicio 12")
print("Resultado:")
miFrase = "Ha hecho una mañana maravillosa"
print(f"           Las palabras de mi frase  {miFrase}  tienen las siguientes longitudes: {HallarLongitudesPalabras(miFrase)}")

""" 
13 Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
"""
def mayus_minus_unicas(cadena):
    """Función que devuelve cada letra de una cadena de texto en mayusculas y minusculas

    Args:
        cadena (str): cadena de texto

    Returns:
        list: lista de tuplas con las letras de una cadena de texto en mayusculas y minusculas
    """
    unicas = set(cadena)  # eliminamos los  duplicados al convertir en set
    resultado = list(map(lambda c: (c.upper(), c.lower()), unicas)) 
    return resultado

#Probamos
texto = "asdhujiudhfjsdr fdhsdfjbcx"
print("Ejercicio 13")
print("Resultado:")
print(f"           En mi conjunto de caracteres:  {miFrase}")
print(f"            los caracteres que aparecen en mayusculas/minúsculas son: " + str(mayus_minus_unicas(texto)))

"""
14 Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
función filter()
"""
def BuscarPalabras(listaPalabras,letra):
    """Función que busca palabras que comienzan por un carácter

    Args:
        listaPalabras (str): lista con las palabras en las que queremos buscar
        letra (str): Carácter con el que tiene que empezar la palabra que buscamos

    Returns:
        list: lista de palabras que comienzan por la letra especificada
    """
    #Filtramos la listaPalabras que pasamos como atributo con la condición que tiene que empezar por la letra pasada
    listaFiltrada = list(filter(lambda palabra: palabra.startswith(letra), listaPalabras))
    return listaFiltrada


#Probamos
milistaPalabras = ["camión", "cuna", "coche", "avión", "deportivo", "manzana", "espalda", "jamón", "barco", "biberón"]
print("Ejercicio 14")
print("Resultado:")
miLetra = "c"
print(f"        Las palabras de mi lista que empiezan por {miLetra} son: " + str(BuscarPalabras(milistaPalabras,miLetra)))



"""
15 Crea una función lambda que  sume 3 a cada número de una lista dada.
"""
def Sumar3_a_Lista(listaNumeros):
    """Función que suma 3 a una lista de números

    Args:
        listaNumeros (list): lista con los números que deseamos

    Returns:
        list: lista resultado de sumar 3 a cada componente de la lista proporcionada
    """
    listaNumeros = list(map(lambda numero: numero + 3,listaNumeros))
    return listaNumeros

#Probamos
miListaNumeros4 = [3,4,2,5,7,89,12]
miNuevaLista = Sumar3_a_Lista(miListaNumeros4)
print("Ejercicio 15")
print("Resultado:")
print(f"     El resultado de sumar a cada valor de la lista de numeros {miListaNumeros4} el valor 3 es: " + str(Sumar3_a_Lista(miListaNumeros4)))


"""
16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
todas las palabras que sean más largas que n. Usa la función 
filter()
"""
def BuscarPalabrasLargas(texto,longPalabras):
    """Función que busca en un texto palabras con una longitud mayor a una dada

    Args:
        texto (str): cadena de texto en la que buscar
        longPalabras (int): longitud de las palabras a buscar

    Returns:
        list: lista con las palabras que exceden de la longitud de palabras
    """
    #Primero separamos el texto en una lista de palabras
    palabras = texto.split()
    
    listaFiltrada = list(filter(lambda palabra: len(palabra) > longPalabras,palabras))
    return listaFiltrada

#Probamos
miTexto = "En un lugar de la mancha de cuyo nombre no me acuerdo"
miLongitud = 3
print("Ejercicio 16")
print("Resultado:")
print(f"     Las palabras de mi texto {miTexto} que exceden de la longitud {miLongitud} son " + str(BuscarPalabrasLargas(miTexto,miLongitud)))


"""
17 Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos 572. Usa la función reduce()
"""
#Importamos la función reduce de la librería functools
from functools import reduce

def UnirListaNumeros(listNumeros):
    #definimos nuestra función que le pasamos como argumento una lista de números
    # devolvemos el resultado de ejecutar una lambda que usa un acumulador para cada
    # uno de los dígitos que vamos multiplicando por 10 en cada paso, y para que lo
    # haga con todos los dígitos usamos la función reduce    
    return reduce(lambda acumulado, digito: acumulado*10+digito,listNumeros)


miListaNumeros5 = [5,7,2]
print("Ejercicio 17")
print("Resultado:")
print(f"    El resultado de unir los digitos de la lista {miListaNumeros5} es: " + str(UnirListaNumeros(miListaNumeros5)))


"""
 18 Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
90. Usa la función filter()
"""
#Definimos nuestros alumnos
alumno1 = dict(nombre="Alberto",edad=23,calificación=40)
alumno2 = dict(nombre="Germán",edad=27,calificación=60)
alumno3 = dict(nombre="Sofía",edad=21,calificación=100)
alumno4 = dict(nombre="Ismael",edad=25,calificación=20)
alumno5 = dict(nombre="Javier",edad=22,calificación=70)
alumno6 = dict(nombre="Luis",edad=24,calificación=95)
listaAlumnos = [alumno1,alumno2,alumno3,alumno4,alumno5,alumno6]

alumnosMasNota = list(filter(lambda alumno: alumno["calificación"]>=90,listaAlumnos))

print("Ejercicio 18")
print("Resultado:")
print(f"    Los alumnos con una nota mayor o igual a 90 son: {alumnosMasNota}")


"""
 19 Crea una función lambda que filtre los números impares de una lista dada.
"""
#Definimos nuestra lista de números
miListaNumeros6 = [1,4,5,23,44,56,66,77,82,91,99]

miListaNumerosImpares = list(filter(lambda numero:numero%2 != 0,miListaNumeros6))
print("Ejercicio 19")
print("Resultado: ")
print(f"    En la lista {miListaNumeros6} los números impares son: " + str(miListaNumerosImpares))


"""
20 Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
"""
#definimos una lista mixta de integer y string
miListaIntStr = [23,22,11,"hola","adios"]
#Usamos la función filter, y en el campo función usamos una lambda que comprueba que cada elemento de la lista inicial es un integer
miListaSoloInt = list(filter(lambda elemento: isinstance(elemento,int),miListaIntStr))

print("Ejercicio 20")
print("Resultado: ")
print(f"     En la lista {miListaIntStr}, los elementos que son integer son: " + str(miListaSoloInt))


"""
 21 Crea una función que calcule el cubo de un número dado mediante una función lambda
"""
miNumero2 = 4
AlCubo = lambda n: n ** 3

print("Ejercicio 21")
print("Resultado: ")
print(f"     El cubo del número {miNumero2} es: " + str(AlCubo(miNumero2)))


"""
22  Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce() .
"""
#Importamos la librería functools para acceder a la función reduce
from functools import reduce

#Definimos nuestra lista de números
miListaNumeros7 = [2,5,89,12,6]

elProductoNumeros = reduce(lambda n1,n2: n1*n2,miListaNumeros7)

print("Ejercicio 22")
print("Resultado: ")
print(f"     El producto de la lista de números {miListaNumeros7} es: " + str(elProductoNumeros))


"""
23 Concatena una lista de palabras.Usa la función reduce() .
"""
#Definimos nuestra lista de palabras
miListaPalabras = ["Cojín", "cama","mesa", "silla", "ordenador"]
#usamos la función reduce que recibe como parámetro una función lambda que concatena dos elementos y la lista de palabras
palabras = reduce(lambda p1,p2: p1 + " " +p2,miListaPalabras)

print("Ejercicio 23")
print("Resultado: ")
print(f"     La unión de la lista de palabras {miListaPalabras} es: " + palabras)


"""
24 Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
"""
#definimos nuestra lista de números
miListaNumeros8 = [12,34,52,112,321]
# Usando la función reduce, le pasamos como primer atributo una función lambda que resta dos parámetros
# y como segundo atributo le pasamos la lista de números
laDiferencia = reduce(lambda n1,n2: n1-n2,miListaNumeros8)

print("Ejercicio 24")
print("Resultado: ")
print(f"     La diferencia entre todos los números de la lista  {miListaNumeros8} es: " + str(laDiferencia))

"""
25 Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""
def esCaracter(caracter):
    """Función que devuelve si un caracter pertenece a los caracteres imprimibles

    Args:
        caracter (str): caracter a analizar

    Returns:
        bool: resultado de chequear si el caracter es un número del 0-9;una letra minúscula/mayúscula del abecedario
    """
    # - número = 0-9
    esNumero =  (ord(caracter) >= 48) and (ord(caracter) <= 57)
    # - letra minúscula = a..z + ñ 
    esLetraMinuscula = ((ord(caracter) >= 97) and (ord(caracter) <= 122) or (ord(caracter) == 164))
    # - letra mayúscula = A..Z + Ñ
    esLetraMayuscula = ((ord(caracter) >= 65) and (ord(caracter) <= 90) or (ord(caracter) == 165))
    # - vocal acentuada = á,é,í,ó,ú,Á,É,Í,Ó,Ú,ü,Ü
    esVocalAcentuada = caracter in "áéíóúÁÉÍÓÚüÜ"
    #devolvemos que es un caracter si cumple alguna de las condiciones anteriors
    return esNumero or esLetraMinuscula or esLetraMayuscula or esVocalAcentuada
    

# Definimos nuestra cadena de texto
miCadena2 = "Como me gusta el verano"
# Vamos a contar los caracteres que sean letras o números, obviando los signos de puntuación, espacios, etc
# Para ello usaremos al función filter, que le pasamos la función que hemos definido más arriba
# para que cada caracter de la cadena de texto que hemos definido, lo analice y nos lo devuelva. 
# Lo convertimos en lista y aplicamos la función len.
longitud = len(list(filter(esCaracter,miCadena2)))

print("Ejercicio 25")
print("Resultado: ")
print(f"    La cadena de texto <{miCadena2}>  tiene {longitud} caracteres")


"""
26 Crea una función lambda que calcule el resto de la división entre dos números dados.
"""
#Definimos dos números
dividendo = 45
divisor = 8

resto = (lambda dividendo,divisor: dividendo%divisor)(dividendo,divisor)

print("Ejercicio 26")
print("Resultado: ")
print(f"    El resto en la división entre {dividendo} y {divisor} es: {resto}")

"""
27 Crea una función que calcule el promedio de una lista de números.
"""
# Definimos una función que nos va a calcular la suma de todos los valores de la lista que le pasamos como atributo "sum(lista)"
# y lo intentamos dividir por la longitud de la lista, en caso que la longitud sea 0, lanzamos un error
def fPromedio(listaNum):
    """Función para calcular el promedio de los valores pasados en una lista, si es posible

    Args:
        listaNum (list): Lista de números de los que queremos obtener el promedio

    Returns:
        float: Valor promedio
    """
    media = 0
    try: #Intentamos hacer la media de los valores de la lista
        media =sum(listaNum)/len(listaNum)
    except ZeroDivisionError: #Gestionamos la excepción de dividir por 0
        print("Error: La lista no tiene componentes")
    else:   #En caso de ser correcto
        return media
    
miListaNumeros9 = [3,65,78,1,12,34,76]
promedio = fPromedio(miListaNumeros9)
print("Ejercicio 27")
print("Resultado: ")
print(f"    El promedio de la lista de números {miListaNumeros9} es: {promedio}")


"""
28 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""
def encuentraPrimerDuplicado(miLista):
    # Función que recibe como argumento una lista de elementos
    # Creamos una lista auxiliar para ir guardando los elementos
    recorridos = []
    for elemento in miLista:
        # Para todos los elementos que tiene la lista
        # chequeamos si el elemento está ya en la lista auxiliar 
        if elemento in recorridos:
            #Si el elemento está ya guardado, hemos encontrado el primer duplicado
            return elemento
        #Si el elemnento no está en la lista auxiliar lo añadimos
        recorridos.append(elemento)
    # En caso de no haber duplicado devolvemos None
    return None

miListaPruebas = [1,43,2,1,4,43]
print("Ejercicio 28")
print("Resultado: ")
print(f"     En la lista {miListaPruebas} el primer elemento duplicado es: " + str(encuentraPrimerDuplicado(miListaPruebas)) )


"""
29 Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro.
"""
def enmascararPwd(pwd):
    # Le pasamos como argumento la variable texto que queremos enmascarar
    mascara = "####"    #Definimos los caracteres que queremos poner en lugar de los originales
    return mascara + pwd[4::1]  #Devolvemos la máscara + la parte de la varible pwd a partir de 5 caracter

miPwd = "12345678"
print("Ejercicio 29")
print("Resultado: ")
print("La contraseña enmascarada es: " + enmascararPwd(miPwd))

"""
30 Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.
"""
def sonAnagramas(p1,p2):
    if (p1 != p2) and (sorted(p1) == sorted(p2)):
        #Son palabras distintas y contienen las mismas letras
        return True

    else:
        return False

pal1 = "sergio"    
pal2 = "riesgo"

print("Ejercicio 30")
print("Resultado: ")
print(f"     ¿Las palabras {pal1}-{pal2} son anagramas? La respuesta es:  " + str(sonAnagramas(pal1,pal2)))



"""
31 Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
lanza una excepción.
"""
def PedirListaNombres():
    #Inicializamos variables locales para controlar la función
    numNombres = 0
    terminar = False
    hayQuePedirNombre = ""
    listaNombres = []

    #Generamos un bucle que se repite hasta que el usuario del programa pulse N al preguntarle si quiere introducir un nuevo nombre
    while not terminar:
        hayQuePedirNombre = input(f"¿Quiere introducir un nuevo nombre en su lista? Hay: {numNombres} actualmente. Pulse S (Sí) o N (No)")
        if hayQuePedirNombre == "S":
            nombre = str(input("Introduzca el nombre del usuario: "))
            listaNombres.append(nombre)
            numNombres += 1
            terminar = False
        elif hayQuePedirNombre == "N": #el usuario ha pulsado que no quiere seguir introduciendo nombres
            terminar = True
        else: #EL usuario ha pulsado una opción NO válida
            print("Opción inválida")
            terminar = False

    return listaNombres #Devolvemos la lista de nombres

def buscarNombre(itemBuscado,listaDeBusqueda):
    return itemBuscado in listaDeBusqueda

#Pruebas
print("Ejercicio 31")

miListaNombres = []
print(" A continuación debe introducir un listado de nombres de 1 en 1 según se le pida")
miListaNombres = PedirListaNombres()
print("Los nombres de la lista son " + str(miListaNombres))

nombreBuscado = input("Introduzca un nombre para buscar en la lista")

if nombreBuscado in miListaNombres:
    print(f"El nombre {nombreBuscado} se ha encontrado")
else:
    print(f"El nombre buscado {nombreBuscado} no se ha encontrado")


"""
32 Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.
""" 
def BuscarEmpleado(nombre,lista):
    if nombre in lista:
        print(f"El puesto del trabajador {nombre} es: " + str(lista.index(nombre)))
    else:
        print(f"{nombre} no trabaja aquí")


miNombreCompleto = "Julian García"
milistaEmpleados = ["Lisa Simpson","Luis Alegre","Jaime Perez","Julian García","Maite Pérez"]

print("Ejercicio 32")
BuscarEmpleado(miNombreCompleto,milistaEmpleados)

 
 
""" 
33 Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""
miListaNumeros10 = []
miListaNumeros11 = []

for n in range(0,29,1):
    miListaNumeros10.append(n)

for n in range(49,20,-1):
    miListaNumeros11.append(n)

sumaMisListas = list(map(lambda x, y: x + y, miListaNumeros10, miListaNumeros11))

print("Ejercicio 33")
print("La suma de la lista de números " + str(miListaNumeros10) + " y la lista de números " + str(miListaNumeros11) + " es:")
print(str(sumaMisListas))


"""
34 Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
            crecer_tronco , 
            nueva_rama , 
            crecer_ramas , 
            quitar_rama e 
            info_arbol . 
    El objetivo es implementar estos métodos para manipular la estructura del árbol.
        Código a seguir:
            1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
            2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
            3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
            4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
            5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
            6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
    Caso de uso:
        1. Crear un árbol.
        2. Hacer crecer el tronco del árbol una unidad.
        3. Añadir una nueva rama al árbol.
        4. Hacer crecer todas las ramas del árbol una unidad.
        5. Añadir dos nuevas ramas al árbol.
        6. Retirar la rama situada en la posición 2.
        7. Obtener información sobre el árbol.
"""
#Definimos nuestra clase
class Arbol:
    """Clase arbol
    """
    #Metodo constructor con los atributos tronco y ramas
    def __init__(self,tronco,ramas=None):
        """
        Args:
            tronco (int): La longitud del tronco
            ramas (int): Lista con la longitud de cada rama, inicializada a None
        """    
        #Creamos los atributos y asignamos el valor de los parámetros del método constructor
        self.tronco = tronco
        self.ramas  = ramas if ramas is not None else []
    
    def crecer_tronco(self,cuanto):
        """Metodo para crecer el tronco.
        
        Args:
            cuanto (int): lo que tiene que crecer
        """
        self.tronco += cuanto
    
    def nueva_rama(self,long):
        #método para añadir una nueva rama a nuestra lista
        #Arg: long --> longitud de la nueva rama
        self.ramas.append(long)

    def crecer_ramas(self,incLong):
        #método para hacer crecer todas nuestras ramas
        #Arg: inclong --> longitud que se incrementan todas las ramas
        self.ramas = [long + incLong for long in self.ramas]
    
    def quitar_rama(self,i):
        #método para quitar una rama en concreto
        #Arg: i --> indice de la rama que hay que eliminar

        #Vamos a chequear que se le pasa un índice válido
        if i > 0 and i < len(self.ramas):
            self.ramas.pop(i)
        else:
            print(f"Indice {i} no válido")

    def info_arbol(self):
        #método para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes
        print("La información del arbol deseado es:")
        print(f"El tronco mide: {self.tronco} metros")
        print("El árbol tiene: " + str(len(self.ramas)) + " ramas")
        print("Cada rama mide: ")
        for i,rama in enumerate(self.ramas):
            print(f"La rama numero {i} mide {rama}")

print("Ejercicio 34")
#Creamos el arbol, con tamaño 1 de tronco y 3 ramas
miArbol = Arbol(0,[1,3,2])
#Hacemos crecer el tronco en 1 unidad
miArbol.crecer_tronco(1)
#Añadimos una nueva rama
miArbol.nueva_rama(3)
#Hacemos crecer todas las ramas
miArbol.crecer_ramas(1)
#Añadimos 2 ramas nuevas
miArbol.nueva_rama(1)
miArbol.nueva_rama(5)
#Quitamos la rama de la posición 2 --> indice 1
miArbol.quitar_rama(1)

miArbol.info_arbol()



"""
35 Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
agregar dinero al saldo.
    Código a seguir:
    1 Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
    2 Implementar el método True y False .
     retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no 
        poder hacerse.
    3 Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
        Lanzará un error en caso de no poder hacerse.
    4 Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
    Caso de uso:
        Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 
        Agregar 20 unidades de saldo de "Bob".
        Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
        Retirar 50 unidades de saldo a "Alicia".
"""
class UsuarioBanco:

    def __init__(self,nombre,saldo=0.0,tieneCuenta=False):
        """
        Args:
            nombre (string): Nombre del cliente
            saldo (float): Saldo que dispone el cliente
            tieneCuenta (bool): True= Tiene cuenta activa
        """    
        #Creamos los atributos y asignamos el valor de los parámetros del método constructor
        self.nombre = nombre
        self.saldo  = saldo
        self.tieneCuenta = tieneCuenta

    def retirar_dinero(self,cantidad):
        """
        Args:
            cantidad (float): Cantidad que se quiere retirar
        Return:
            Saldo que hay en la cuenta
        """
        if  self.saldo < cantidad:
            print(f"El usuario {self.nombre} no dispone de suficiente saldo. Su saldo actual es: {self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"El saldo actual de {self.nombre} es: {self.saldo}")
        return self.saldo

    def transferir_dinero(self,cantidad,UsuarioOrigen):
        """
        Args:
            cantidad (float): Cantidad de dinero que se va a transferir desde el UsuarioOrigen
            UsuarioOrigen (UsuarioBanco): Usuario de banco desde el que se transfiere la cantidad y se le actualiza el importe de su saldo
        Return: 
            Saldo (float) que hay en la cuenta
        """
        if UsuarioOrigen.saldo < cantidad:
            print(f"El usuario {UsuarioOrigen.nombre} no dispone de suficiente saldo")
        else:
            UsuarioOrigen.saldo -= cantidad
            self.saldo += cantidad
            print(f"Se ha procedido a realizar la transferencia, el usuario {self.nombre} tiene un saldo de: {self.saldo}")
        return self.saldo            

    def agregar_dinero(self,cantidad):
        """
        Args:
            cantidad (float): Cantidad que se quiere retirar
        Return:
            Saldo que hay en la cuenta
        """
        self.saldo += cantidad
        print(f"Se ha agregado la cantidad de {cantidad} € a la cuenta de {self.nombre} con un saldo final de: {self.saldo}")
        return self.saldo
        
print("Ejercicio 35")
uAlicia = UsuarioBanco("Alicia",100.0,True)
uBob    = UsuarioBanco("Bob",100.0,True)
print(f"El usuario {uAlicia.nombre} tiene un saldo de {uAlicia.saldo}")
print(f"El usuario {uBob.nombre} tiene un saldo de {uBob.saldo}")

saldo = uBob.agregar_dinero(20)

saldo = uAlicia.transferir_dinero(80,uBob)
print(f"El saldo de Alicia es: {saldo} y el de Bob es: {uBob.saldo}")

saldo = uAlicia.retirar_dinero(50.0)



"""
 36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
    reemplazar_palabras , 
    procesar_texto .
    contar_palabras , 
    eliminar_palabra . 
    Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 
    
    Código a seguir:
        1 Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. 
        Tiene que devolver un diccionario.
        2 Crear una función reemplazar_palabras para remplazar una que devolver el texto con el remplazo de palabras.
        3 Crear una función palabra_original del texto por una palabra_nueva . 
        Tiene eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
        4 Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
        número de argumentos variable según la opción indicada.
    Caso de uso:
        Comprueba el funcionamiento completo de la función procesar_texto
"""        
import re

def contarPalabras(texto):
    """
    Función que cuenta las veces que aparece cada palabra en un texto

    Args:
        texto (str): texto del cual queremos contar las palabras

    Returns:
        diccionario : Diccionario con las palabras que aparecen en el texto y el número de apareciones
    """
    #Convertimos el texto todo en minusculas
    texto = texto.lower()

    #Sustituimos los signos de puntuación por " "
    for caracter in ",.;:!¡¿?'[]":
        texto = texto.replace(caracter, " ")

    #Separamos todas las palabras a una lista
    misPalabras = texto.split()

    #Creamos el diccionario que devolveremos
    miDiccionario = {}
    for palabra in misPalabras:
        if palabra in miDiccionario:
            miDiccionario[palabra] += 1
        else:
            miDiccionario[palabra] = 1

    #devolvemos el diccionario creado    
    return miDiccionario

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Función que reemplazará a una palabra completa por otra y nos devolverá el texto modificado

    Args:
        texto (str): Texto en el que queremos sustituir una palabra
        palabra_original (str): Palabra que queremos encontrar para sustituir
        palabra_nueva (str): Palabra que sustituimos

    Returns:
        str: El texto modificado
    """

    # Vamos a usar la librería re.
    # Definimos un patrón para identificar las palabras. Usamos \b para que coincida solo con palabras completas (bordes de palabra)
    patron = r'\b' + re.escape(palabra_original) + r'\b'
    # Usamos el flag "IgnoreCase" para que no tenga en cuenta mayúsculas/minúsculas
    texto_reemplazado = re.sub(patron, palabra_nueva, texto,flags=re.IGNORECASE)

    return texto_reemplazado


def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Función para eliminar una palabra de un texto dado. No se distingue entre mayúsculas/minúsculas

    Args:
        texto (str): Texto del que se quiere eliminar una palabra en concreto
        palabra_a_eliminar (str): palabra que hay que buscar para eliminar

    Returns:
        str: el texto dado con la palabra eliminada
    """
    # Creamos un patrón que coincida con la palabra completa, sin importar mayúsculas/minúsculas
    patron = r'\b' + re.escape(palabra_a_eliminar) + r'\b'
    
    # Reemplazamos con cadena vacía (usando flag IGNORECASE para que ignore posibles palabras con mayuscula inicial)
    texto_sin_palabra = re.sub(patron, '', texto, flags=re.IGNORECASE)
    
    # Limpiamos espacios dobles que podemos haber generado, para que quede el texto más limpio
    texto_limpio = re.sub(r'\s{2,}', ' ', texto_sin_palabra).strip()
    
    return texto_limpio

#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") 
#   y un número de argumentos variable según la opción indicada.    
def procesar_texto(texto,opc,*args):
    """
    Función para poder procesar un texto

    Args:
        texto (str): texto que se quiere procesar
        opc (str): "contar","reemplazar","eliminar"
        *args (tuple): en función de la opción seleccionada
                -"contar": Ningún argumento adicional
                -"reemplazar": palabra_original(str)--> Palabra a buscar
                               palabra_nueva(str) --> Palabra que sustituye  
                -"eliminar": palabra_a_eliminar (str) --> Palabra que queremos eliminar del texto
    """
    if opc == "contar":
        return contarPalabras(texto)
    
    elif opc == "reemplazar":
        if len(args) != 2:
            raise ValueError("La función 'reemplazar' necesita de 2 argumentos: palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif opc == "eliminar":
        if len(args) != 1:
            raise ValueError("La función 'eliminar' necesita 1 argumento: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")
    

# Definimos nuestro texto
print("Ejercicio 36")
texto = "El lenguaje de programación Python es del tipo orientado a objetos. Esto quiere decir que está construido alrededor de un tipo especial de entidad, un objeto, que contiene a la vez datos así como una serie de métodos para acceder y alterar los datos. Una vez que se crea un objeto se puede interactuar con otros objetos."

terminar = False
# Generamos un bucle que nos va a permitir realizar más de una operación sin terminar el programa
while not terminar:
    Opcion = input("Elija la opción que desee: contar,reemplazar,eliminar")
    #Analizamos la opción elegida por el usuario y ejecutamos el programa adecuado
    if Opcion == "contar":
        misPalabras = {}
        misPalabras = procesar_texto(texto,Opcion)
        print(f"el listado de palabras del texto es: {misPalabras}")
    elif Opcion == "reemplazar":
        palabra_A_Reemplazar = input("Introduzca la palabra a reemplazar")
        palabra_Nueva = input(f"Introduzca la palabra por la que reemplaza {palabra_A_Reemplazar}")
        miTexto = procesar_texto(texto,Opcion,palabra_A_Reemplazar,palabra_Nueva)
        print(f"El texto modificado es: {miTexto}")
    elif Opcion == "eliminar":
        palabra_A_Eliminar = input("Introduzca la palabra a eliminar")
        miTexto = procesar_texto(texto,Opcion,palabra_A_Eliminar)
        print(f"El texto modificado es: {miTexto}")
    else:
        print(f"Opcion {Opcion} no está aceptada entre")

    opcionvalida = False
    while not opcionvalida:
        Finalizar = input("¿Desea ejecutar otra acción? Sí pulse S/ No pulse N")
        if Finalizar.lower() == "n":
            terminar = True
            opcionvalida = True
        elif Finalizar.lower() == "s":
            terminar = False
            opcionvalida = True
        else:
            terminar = False
            opcionvalida = False        
        

"""
37. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
"""
# Dividiremos el día en tres franjas, desde las 00:00 hasta las 6:00 y de las 22:00 a las 24:00 consideraremos que 
# es de noche, de 6:00 a 14:00 consideraremos que es de día (o de mañanas) y de 14:00 a 22:00 consideraremos que
# es de tardes. 

def determinar_turno(hora):
    """Función para determinar en que momento del día nos encontramos en función de una hora introducida

    Args:
        hora (int): Hora que queremos analizar

    Returns:
        (str) : El turno en el que nos encontramos
    """
    if 6 <= hora < 14:
        return "Es turno de mañana."
    elif 14 <= hora < 22:
        return "Es turno de tarde."
    else:
        return "Es turno de noche."

def solicitar_hora():
    """Función para solicitar la hora al usuario en formato 00-23

    Returns:
        int : Hora introducida por el usuario
    """
    while True:
        entrada = input("Introduce la hora (de 0 a 23): ")
        if entrada.isdigit():
            hora = int(entrada)
            if 0 <= hora <= 23:
                return hora
            else:
                print("La hora debe estar entre 0 y 23.")
        else:
            print("Por favor, introduce un número válido.")

print("Ejercicio 38")
hora = solicitar_hora()
turno = determinar_turno(hora)
print(turno)



"""
39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""
# Definiremos dos funciones

def obtener_calificacion_texto(nota):
    """Función para convertir una nota numérica en una interpretación en texto

    Args:
        nota (int): Nota numérica del alumno

    Returns:
        str: texto interpretativo de la nota
    """
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación fuera de rango (0-100)"

def solicitar_calificacion():
    """Función para pedir la nota a analizar al usuario

    Returns:
        int: Nota introducida por el usuario entre 0-100
    """
    while True:
        entrada = input("Introduce la calificación del alumno (0-100): ")
        if entrada.isdigit():
            nota = int(entrada)
            return nota
        else:
            print("Por favor, introduce un número válido entre 0 y 100.")

print("Ejercicio 39")
# Programa principal
nota = solicitar_calificacion()
calificacion = obtener_calificacion_texto(nota)
print(f"La calificación del alumno es: {calificacion}")




"""
40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
"""
# Importamos la función math para tener acceso al número pi
import math

#Definimos dos funciones, una para solicitar los datos de la figura introducida en un primer promt, y 
# otra para calcular el área
def calcular_area(figura, datos):
    """Función que calcula el área de una figura (rectangulo,circulo o triangulo)

    Args:
        figura (str): tipo de figura a calcular el área
        datos (tuple): tupla con los datos relevantes de la figura

    Returns:
        float: área de la figura
    """
    figura = figura.lower()

    if figura == "rectangulo":
        if len(datos) != 2:
            return "Se necesitan base y altura para un rectángulo."
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            return "Se necesita el radio para un círculo."
        (radio,) = datos
        return math.pi * radio**2

    elif figura == "triangulo":
        if len(datos) != 2:
            return "Se necesitan base y altura para un triángulo."
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no reconocida. Usa 'rectangulo', 'circulo' o 'triangulo'."
    
def solicitar_datos(figura):
    """Función para solicitar los datos necesarios en base a la figura
    Args:
        figura (str): tipo de figura a calcular el área

    Returns:
        tuple : tupla con los datos de la figura
    """
    figura = figura.lower()

    if figura == "rectangulo":
        try:
            base = float(input("Introduce la base del rectángulo: "))
            altura = float(input("Introduce la altura del rectángulo: "))
            return (base, altura)
        except ValueError: #En caso de introducir un valor no numérico levantamos una incidencias
            print("Entrada inválida. Usa números.")
            return None

    elif figura == "circulo":
        try:
            radio = float(input("Introduce el radio del círculo: "))
            return (radio,)
        except ValueError: #En caso de introducir un valor no numérico levantamos una incidencias
            print("Entrada inválida. Usa un número.")
            return None

    elif figura == "triangulo":
        try:
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            return (base, altura)
        except ValueError: #En caso de introducir un valor no numérico levantamos una incidencias
            print("Entrada inválida. Usa números.")
            return None

    else:
        print("Figura no reconocida.")
        return None

print("Ejercicio 40")
figura = input("Elige una figura (rectangulo, circulo, triangulo): ").strip().lower()
datos = solicitar_datos(figura)

if datos:
    area = calcular_area(figura, datos)
    print(f"El área del {figura} es: {area}")




""" 
41 En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
siguiente:
 1. Solicita al usuario que ingrese el precio original de un artículo.
 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python
"""
def aplicar_descuento():
    try:
        precio_original = float(input("Introduce el precio original del artículo (€): "))
        if precio_original <= 0:
            print("El precio debe ser mayor a cero.")
            return

        tiene_cupon = input("¿Tienes un cupón de descuento? (sí / no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            try:
                valor_descuento = float(input("Introduce el valor del cupón (€): "))
                if valor_descuento > 0:
                    precio_final = max(0, precio_original - valor_descuento)
                    print(f"Se ha aplicado un descuento de {valor_descuento:.2f}€.")
                else:
                    print("El valor del cupón no es válido. Se cobrará el precio original.")
                    precio_final = precio_original
            except ValueError:
                print("El valor introducido no es válido. Se cobrará el precio original.")
                precio_final = precio_original
        elif tiene_cupon == "no":
            precio_final = precio_original
        else:
            print("Respuesta no válida. Se asume que no hay cupón.")
            precio_final = precio_original

        print(f"El precio final de la compra es: {precio_final:.2f}€")
    
    except ValueError:
        print("Error: Debes introducir un número válido para el precio.")

# Ejecutar el programa
aplicar_descuento()


