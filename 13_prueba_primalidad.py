def es_primo(numero):
    contador = 0

    for i in range(1, numero +1): # ponemos numero+1 porque range va hasta el numero-1, necesitamos llegar a numero 
        if i==1 or i==numero:
            continue
        if numero % i == 0:
            contador += 1
    print(str(numero) + " " + str(contador))
    if contador == 0 and not numero == 1:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()