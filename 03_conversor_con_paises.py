menu = """
Bienvenido al conversor de monedas 馃挵
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opci贸n: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("驴Cu谩ntos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
elif opcion == 2:
    pesos = input("驴Cu谩ntos pesos nargentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
elif opcion == 3:
    pesos = input("驴Cu谩ntos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
else:
    print("Ingresa una opci贸n correcta por favor")