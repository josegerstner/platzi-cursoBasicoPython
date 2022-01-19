from calendar import c
from threading import currentThread


def run():
    contador = 0
    cuantas_aparece = 0
    frase = input("Escriba una frase: ")
    aparece = input("Ingrese la letra que quiera contar: ")
    termina = input("Ingrese la letra para terminar: ")

    while(contador < len(frase)):

        if frase[contador] == termina:
            print("Se termina la ejecución")
            break

        print(frase[contador])
        contador += 1

        if frase[contador] != aparece:
            continue

        cuantas_aparece+=1
        print("La letra " + aparece + " aparece " + str(cuantas_aparece) + " veces... hasta ahora")


if __name__ == '__main__':
    run()