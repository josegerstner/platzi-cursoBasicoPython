from calendar import c


def run():
    contador = 0
    cuantas_aparece = 0
    frase = input("Escriba una frase: ")
    aparece = input("Ingrese la letra que quiera contar: ")
    termina = input("Ingrese la letra para terminar: ")

    while(frase[contador]):

        if frase[contador-1] == termina:
            break

        print(frase[contador])
        if frase[contador] == aparece:
            continue
        cuantas_aparece+=1
        
        contador += 1
            

if __name__ == '__main__':
    run()