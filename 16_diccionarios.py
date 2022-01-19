

from re import S


def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3
    }

    # imprimo el diccionario
    # print(mi_diccionario)
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }

    # print(poblacion_paises["Argentina"])

    # Recorremos el diccionario desde las llaves 
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # Recorremos el diccionario desde los valores
    # for pais in poblacion_paises.values():
    #     print(pais)

    # Recorremos el diccionario desde las llaves y los valores
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")



if __name__ == '__main__':
    run()