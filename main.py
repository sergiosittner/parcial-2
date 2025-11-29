import random
from categorias import *

#----------------------------(FUNCIÓN PARA VER UN MENU)-------------------------------------------------

def mostrar_menu():
    print("=============== \n MENU GENERALA \n===============")
    print("1) Jugar")
    print("2) Estadísticas")
    print("3) Créditos")
    print("4) Salir")


#-------------------------------------------(FUNCIÓN PARA TIRAR DADOS)----------------------------------

def tirar_dados(numero_de_dados, cara_inicial, cara_final):
    lista_auxiliar = []
    for i in range(numero_de_dados):
        lista_auxiliar.append(random.randint(cara_inicial, cara_final))

    print(f"Tirada de dados: {lista_auxiliar}")
    return lista_auxiliar

#-------------------(FUNCIÓN PARA ELEGIR DADOS)-----------------------------------------------------

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


#-----------------------------------(FUNCIÓN PARA AGRUPAR LOS DADOS ELEGIDOS)---------------------------------


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


#---------------------------------------------(FUNCION PARA ELEGIR EN QUE CATEGORIA ANOTAR LOS DADOS)-------------------------------------------


def seleccionar_categoria(dados, planilla):
    print("\n--- POSIBLES JUGADAS ---")
    

    nombres_categorias = ["1", "2", "3", "4", "5", "6", "ESCALERA", "FULL", "POKER", "GENERALA"]
    

    opciones_disponibles = {}
    indice = 1

    for cat in nombres_categorias:


        puntos_posibles = calcular_puntos(dados, cat)
        
        estado = ""
        if planilla[cat] is not None:
            
            estado = f"Ya anotado ({planilla[cat]} pts)"
        else:
            
            estado = f"-> {puntos_posibles} puntos"
            
            opciones_disponibles[indice] = cat
        
        print(f"[{indice}]: {cat} {estado}")
        indice += 1

    print("--------------------------------------------")
    
    while True:
        entrada = input("Seleccione el número de la categoría para anotar: ")
        
        if not entrada.isdigit():
            print("Ingrese un número válido.")
            continue
            
        seleccion = int(entrada)
        
        if seleccion not in opciones_disponibles:


            if 1 <= seleccion < indice:
                print("Esa categoría ya está ocupada. Elija otra.")
            else:
                print("Opción fuera de rango.")
            continue
            

        categoria_elegida = opciones_disponibles[seleccion]
        puntos_ganados = calcular_puntos(dados, categoria_elegida)
        

        planilla[categoria_elegida] = puntos_ganados
        
        print(f"\n¡Anotado! Sumaste {puntos_ganados} puntos en {categoria_elegida}.")
        return 
    


#----------------------------------(FUNCION CREDITOS)-------------------------------------------
def creditos():
    print("=============== \n MINI GENERALA TEMÁTICA \n===============")
    print("Autores: Agustina Velazquez, Sergio Sittner")
    print("Fecha: Noviembre de 2025")
    print("Materia: Programación 1")
    print("Docentes: Martin Alejandro y Veronica Carbonari")
    print("Carrera: Tecnicatura Universitaria en Programación")
    print("Contacto: sergiosittner05@gmail.com o [falta agregar otro mail]")

#----------------------------------(FUNCION ANOTAR NOMBRE Y PUNTOS EN CSV)----------------------------
def guardar_puntaje(nombre, puntos):
    with open("estadisticas.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntos}\n") 
    print("\nPuntaje guardado correctamente.")

#---------------------------------------(LEER NOMBRES Y PUNTOS DEL ARCHIVO CSV)---------------------------
'''''
def estadisticas():
    print("\n======= ESTADÍSTICAS =======")

    archivo = open("estadisticas.txt", "r")
    contenido = archivo.read()
    archivo.close()

    if contenido.strip() == "":
        print("Todavía no hay partidas registradas.")
    else:
        print(contenido)

    print("============================\n")
'''

def estadisticas():
    print("\n======= TABLA DE POSICIONES =======")
    lista_jugadores = []
    

    with open("estadisticas.txt", "r") as archivo:
        for linea in archivo:

            datos = linea.strip().split(",")
            
            if len(datos) == 2:
                nombre = datos[0]
                puntos_texto = datos[1]
                
                if puntos_texto.isdigit(): 
                    puntos = int(puntos_texto)
                    lista_jugadores.append((nombre, puntos))
    n = len(lista_jugadores)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_jugadores[j][1] < lista_jugadores[j+1][1]:
                x = lista_jugadores[j]
                lista_jugadores[j] = lista_jugadores[j+1]
                lista_jugadores[j+1] = x

    for i, (nombre, puntos) in enumerate(lista_jugadores[:10], start=1):
        print(f"{i}°. {nombre:<15} | {puntos} puntos")

    print("===========================================\n")
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
