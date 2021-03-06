# platzi-cursoBasicoPython  
  
Cosas que se pueden hacer con Python:  
* IOT  
* Inteligencia Artificial  
* Backend  
* Data Science  
  
> Un algoritmo es una serie de pasos ordenados para resolver un problema. Este es finito, ordenado, y no ambiguo  
  
## COMENTARIOS  
  
**#** Para comentar una línea se pone # seguido de un espacio al inicio de la misma.  
  
## OPERADORES MATEMÁTICOS  
> \+ : suma  
> \- : resta  
> \* : multiplicación  
> / : división  
> ** : elevado a (potencia)  
> // : división entera  
> % : módulo  
  
## Funciones útiles (conversión de tipos)  
  
**input**: Le pide al usuario que ingrese un dato (lo toma como tipo texto).  
>Ej: num = input("Escribe un número: ")  
Ingreso: 5  
Resultado: num vale "5"
  
**int**: Convierte una variable a tipo ***int***.  
>Ej: numero1 = "3"  
numero1 = int(numero1)  
Resultado: numero1 vale 3  

**str**: Convierte una variable a tipo texto.  
>Ej: numero1 = 5  
numero1 = str(numero1)  
Resultado: numero1 vale "5"

**float**: Convierte una variable a tipo decimal.  
>Ej: numero1 = "3.14"  
numero1 = float(numero1)  
Resultado: 3.14  

**round**: Redondea la variable del primer parámetro con la cantidad de decimales del segundo parámetro.  
>Ej: round(3.1415, 2)  
Resultado: 3.14.  

**pass**: Me permite dejar código para después.  
>Ej:  
```  
if variable1 == variable2  
    pass  
else:  
    pass  
```  
  
## Operadores lógicos  
  
**and**: Compara dos variables y se cumple sólo si las dos son verdaderas.  
**or**: Compara dos variables y se cumple si alguna de las dos son verdaderas.  
**not**: Invierte el valor de una variable.  
  
## Operadores de comparación  
  
**==** (igual): Compara si dos variables son iguales.  
**!=** (distinto): Compara si dos variables son distintas.  
**>** (mayor): Compara si la primera variable es mayor que la segunda.  
**<** (menor): Compara si la primera variable es menor que la segunda.  
**>=** (mayor o igual): Compara si la primera variable es mayor o igual que la segunda.  
**<=** (menor o igual): Compara si la primera variable es menor o igual que la segunda.  
  
## Condicionales  
  
**if**  
```  
if variable1 > variable2:  
    codigo si se cumple la condición del if  
```  
  
**else**  
```  
if variable1 > variable2:  
    codigo si se cumple la condición del if  
else:  
    codigo si no se cumple el if  
```  

**elif**  
```  
if variable1 > variable2:  
    codigo si se cumple la condición del if  
elif variable1 == variable2:  
    codigo si no se cumple el if pero sí el elif  
else:  
    codigo si no se cumplen las condiciones anteriores  
```  

**NOTA: luego de los dos puntos siempre hay que dejar 4 espacios luego del salto de línea.**  
  
## IMPRIMIR BLOQUE DE TEXTO  
  
>Se puede imprimir bloques de texto. Esto quiere decir, que se puede hacer una variable que contenga muchas líneas de texto. Esto se hace escribiendo dentro de tres comillas dobles:  
```  
menu = """  
Esto es un bloque  
de texto  
:)  
"""  
print(menu)
```  
>La salida de este código será:  
``` 
Esto es un bloque  
de texto  
:)  
```   
  
## FUNCIONES  
  
**def nombre_funcion(parametros):**  
```  
def nombre_funcion(parametros):  
    codigo_de_bloque_de_codigo  
    codigo_de_bloque_de_codigo  
    codigo_de_bloque_de_codigo  
    codigo_de_bloque_de_codigo  
    codigo_de_bloque_de_codigo  
```  
  
## CADENAS DE CARACTERES  
  
Exiten métodos que nos servirán para manipular las cadenas de caracteres cuando sea necesario.  

**cadena.upper()**: Devuelve la cadena con las letras en mayúsculas.  

**cadena.capitalize()**: Devuelve la cadena con la primera letra en mayúscula y las demás en minúsculas.  

**cadena.strip()**: Devuelve la cadena pero quitando los espacios que haya al principio o al final.  

**cadena.lower()**: Devuelve la cadena pero con las letras en minúsculas.  

**cadena.replace(esto, porEsto)**: Devuelve la cadena pero reemplaza lo que hay en _esto_ por lo que hay en _porEsto_.  

**len(cadena)**: Devuelve la cantidad de caracteres que tiene la cadena.  
  
## SLICES (Rebanadas)  
  
**cadena[N:X]**: Devuelve la cadena desde el índice N hasta el caracter anterior al índice X.  
  
**cadena[:X]**: Devuelve la cadena desde el inicio hasta el índice X.  
  
**cadena[X:]**: Devuelve la cadena desde el índice X hasta el final de la cadena.  
  
**cadena[X:N:S]**: Devuelve la cadena desde el índice X hasta el índice N pero en saltos de S en S.  
  
>extra: **cadena[::-1]**: Devuelve la cadena pero invertida.  
  
## BUENA PRÁCTICA: dejar dos espacios entre funciones  
  
## BUCLES  
  
**while condición:**  
>Ej
```  
while x < 10:  
    print('X vale: ' + str(x))  
    x++  
```  
  
**for variable in range(desde, hasta):**  
```  
for x in range(100): # x va de 0 a 99  
    print('X vale: ' + str(x))  
  
for y in range(3, 10): # y va de 3 a 9  
    print('Y vale: ' + str(y))  
```  
  
**for unidad in grupo:**
```  
for letra in nombre:  
        print(letra)  
```  
  
**continue**: Se utiliza en los bucles para dada una condición, si no es cumplida, se ejecuta el siguiente bloque de código dentro del bucle. Sino vuelve al principio del bucle.  
  
**break**: Se utiliza para terminar un bucle cumplida una condición.  
  
## MÓDULOS  
  
>Los módulos son paquetes de código Python que ya vienen con el lenguaje (o no) que podemos importar para utilizar funcionalidades específicas de cada módulo. Se importan arriba del programa con la palabra **import** más el nombre del módulo.  
```  
import módulo  
```  
  
**random**: se utiliza para generar datos aleatorios, por ejemplo números.  
- random.randint(desde, hasta): genera un número entero aleatorio desde el parámetro _desde_ hasta el parámetro _hasta_.  
- random.choise(lista): elige un elemento random de la _lista_.  
  

## LISTAS  
  
>Son objetos ***dinámicos*** que contienen elementos que pueden ser de un tipo de dato, distintos tipos de datos o incluso otros objetos.  
```
lista = [elem1, elem2, ...]
```  
  
**lista[X]**: accede a la posición X de una lista.  
  
**lista.append(algo)**: ingresa _algo_ en la última posición de la lista.  
  
**lista.pop(X)**: elimina el elemento X de una lista.  
  
**for elemento in lista**: recorre todos los elementos de la lista.  
  
>NOTA: Se pueden usar los **slices** en las listas.  
  
## TUPLAS  
  
>Son objetos ***estáticos*** que contienen elementos que pueden ser de un tipo de dato, distintos tipos de dato o incluso otros objetos. Al ser objetos estáticos, no podemos modificarlas una vez creadas. La ventaja que tenemos al usar _tuplas_ por sobre las _listas_ es que es mucho más eficiente el funcionamiento de Python, por ejemplo al iterarlas.  
```py
tupla = (elem1, elem2, ...)
```
  
**tupla(X)**: accedo a la posición X de una tupla.  
  
## DICCIONARIOS  
  
> Un diccionario es una estructura de datos de llaves y valores. En lugar de acceder a sus valores por índices, accedemos a sus valores a través de sus llaves.  
  
```py  
diccionario = {
    "llave": valor,
    ...
}
```  
  
**diccionario[llave]**: accede al contenido de la llave del diccionario.  
  
