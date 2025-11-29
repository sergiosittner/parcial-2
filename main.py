import random
from categorias import *

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
    print("=============== \n MENU GENERALA \n===============")
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

    entrada = input("Ingrese posiciones a conservar (ej: 0,2,4), o ENTER para no conservar: ")


    if entrada.strip() == "":
        return []


    partes = entrada.split(",")

    dados_elegidos = []
    posiciones_usadas = []

    for p in partes:

        p = p.strip() 


        if not p.isdigit():
            print(f"'{p}' no es un número válido.")
            continue

        posicion = int(p)


        if posicion < 0 or posicion >= len(lista_auxiliar):
            print(f"La posición {posicion} está fuera del rango.")
            continue


        if posicion in posiciones_usadas:
            print(f"La posición {posicion} ya fue usada.")
            continue

        posiciones_usadas.append(posicion)
        dados_elegidos.append(lista_auxiliar[posicion])

    print("Dados elegidos:", dados_elegidos)
    return dados_elegidos



def armar_lista_final(tiros, numero_de_dados, cara_inicial, cara_final):
    lista_final = []
    
    while tiros > 0:

        dados_a_tirar = 5 - len(lista_final)
        

        lista_auxiliar = tirar_dados(dados_a_tirar, cara_inicial, cara_final)


        if tiros == 1:

            lista_final.extend(lista_auxiliar)
            print(f"Último tiro completado. Dados finales: {lista_final}")
            break 


        else:

            dados_elegidos = elegir_dados(lista_auxiliar)
            lista_final.extend(dados_elegidos)


            if len(lista_final) == 5:
                break
        
        tiros = tiros - 1

    return lista_final



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
