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
  
