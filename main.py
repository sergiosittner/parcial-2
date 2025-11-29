import random


def menu():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":

            tiros = 3
            numero_de_dados = 5
            cara_inicial = 1
            cara_final = 6

            resultado = armar_lista_final(tiros, numero_de_dados, cara_inicial, cara_final)
            print("Resultado final:", resultado)

        elif opcion == "2":
            estadisticas()

        elif opcion == "3":
            creditos()

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, ingrese nuevamente")


def mostrar_menu():
    print("=============== \n MINI GENERALA \n===============")
    print("1) Jugar")
    print("2) Estadísticas")
    print("3) Créditos")
    print("4) Salir")


def tirar_dados(numero_de_dados, cara_inicial, cara_final):
    lista_auxiliar = []
    for i in range(numero_de_dados):
        lista_auxiliar.append(random.randint(cara_inicial, cara_final))

    print(f"Tirada de dados: {lista_auxiliar}")
    return lista_auxiliar


def elegir_dados(lista_auxiliar):

    dados_elegidos = []
    posiciones_usadas = set()  

    for i in range(len(lista_auxiliar)):

        posicion = input(f"Ingrese posición que desea conservar (0-{len(lista_auxiliar)-1}), o ENTER para no conservar: ")

        if posicion == "":
            continue

        if not posicion.isdigit():
            print("Entrada inválida.")
            continue

        posicion = int(posicion)


        if posicion < 0 or posicion >= len(lista_auxiliar):
            print("Posición fuera de rango.")
            continue


        if posicion in posiciones_usadas:
            print("Esa posición ya fue elegida.")
            continue


        posiciones_usadas.add(posicion)
        dados_elegidos.append(lista_auxiliar[posicion])

        print("Elegidos hasta ahora:", dados_elegidos)

    return dados_elegidos



def armar_lista_final(tiros, numero_de_dados, cara_inicial, cara_final):

    lista_final = []

    while tiros > 0:
        lista_aux = tirar_dados(numero_de_dados, cara_inicial, cara_final)
        elegidos = elegir_dados(lista_aux)

        lista_final.extend(elegidos)
        numero_de_dados -= len(elegidos)
        tiros -= 1


    while len(lista_final) < 5:
        print("Aún faltan elegir dados. Última tirada repetida:")
        lista_aux = tirar_dados(5 - len(lista_final), cara_inicial, cara_final)
        elegidos = elegir_dados(lista_aux)
        lista_final.extend(elegidos)

    return lista_final



def validar_posicion(posicion, posicion_inicial, posicion_final):
    while posicion < posicion_inicial or posicion > posicion_final:
        posicion = int(input("Posición fuera del rango. Ingrese nuevamente: "))
    return posicion



def estadisticas():
    pass


def creditos():
    print("=============== \n MINI GENERALA TEMÁTICA \n===============")
    print("Autores: Agustina Velazquez, Sergio Sittner")
    print("Fecha: Noviembre de 2025")
    print("Materia: Programación 1")
    print("Docentes: Martin Alejandro y Veronica Carbonari")
    print("Carrera: Tecnicatura Universitaria en Programación")
    print("Contacto: sergiosittner05@gmail.com o [falta agregar otro mail]")


menu()
