
def es_primo(numero):
    contador=0
    for i in range(2, numero):
        if numero % i == 0:
            contador+=1
    if contador==0 and not numero==1:
        return True
    else:
        return False

def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == '__main__':
    run()