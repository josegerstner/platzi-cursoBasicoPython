def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if(es_palindromo):
        print("Es palíndromo")
    else:
        print("No es palíndromo")


# Punto de entrada de cualquier programa de paiton
if __name__ == '__main__':
    run()