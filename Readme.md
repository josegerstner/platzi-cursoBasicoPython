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
> ** : elevado a  
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
  
**cadena[N:X]**: Devuelve la cadena desde el índice N (un número) hasta el índice X (que es otro número).  
  
**cadena[X:]**: Devuelve la cadena desde el índice X hasta el final de la cadena.  
  
**cadena[:X]**: Devuelve la cadena desde el inicio hasta el índice X.  
  
**cadena[X:N:S]**: Devuelve la cadena desde el índice X hasta el índice N pero en saltos de S.  
  
