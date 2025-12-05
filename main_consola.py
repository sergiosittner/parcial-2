import pygame
from Lógica_Juego.categorias import *
from Lógica_Juego.dados import *
from Lógica_Juego.puntaje import *

#----------------------------(FUNCIÓN PARA VER UN MENU)-------------------------------------------------

def mostrar_menu():
    print("=============== \n MENU GENERALA \n===============")
    print("1) Jugar")
    print("2) Estadísticas")
    print("3) Créditos")
    print("4) Salir")

#----------------------------------(FUNCION CREDITOS)-------------------------------------------
def creditos():
    print("=============== \n MINI GENERALA TEMÁTICA \n===============")
    print("Autores: Agustina Velazquez, Sergio Sittner")
    print("Fecha: Noviembre de 2025")
    print("Materia: Programación 1")
    print("Docentes: Martin Alejandro y Veronica Carbonari")
    print("Carrera: Tecnicatura Universitaria en Programación")
    print("Contacto: sergiosittner05@gmail.com")

#--------------------------------(FUNCION MENU)---------------------------------------------------

def menu():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":

            turnos_jugados = 0
            

            planilla = {
                "1": None, "2": None, "3": None, "4": None, "5": None, "6": None,
                "ESCALERA": None, "FULL": None, "POKER": None, "GENERALA": None
            }
            
            while turnos_jugados < 3:
                print(f"\n>>> RONDA {turnos_jugados + 1} DE 3 <<<")
                
                tiros = 3
                numero_de_dados = 5
                cara_inicial = 1
                cara_final = 6

                resultado_dados = armar_lista_final(tiros, numero_de_dados, cara_inicial, cara_final)
                print(f"\nDados finales del turno: {resultado_dados}")
                

                seleccionar_categoria(resultado_dados, planilla)
                
                
                puntos_totales = 0
                for puntos in planilla.values():
                    if puntos is not None:
                        puntos_totales += puntos
                
                print(f"PUNTAJE TOTAL ACTUAL: {puntos_totales}")
                
                input("Presione ENTER para continuar a la siguiente ronda...")
                turnos_jugados += 1
                
            print(f"\n¡JUEGO TERMINADO! PUNTAJE FINAL: {puntos_totales}")
            
            nombre = input("Ingrese su nombre para guardar el puntaje: ")
            guardar_puntaje(nombre, puntos_totales)

        elif opcion == "2":
            estadisticas()

        elif opcion == "3":
            creditos()

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, ingrese nuevamente")


menu()
