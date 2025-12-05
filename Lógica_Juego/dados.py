import random
from Lógica_Juego.categorias import *

#-------------------------------------------(FUNCIÓN PARA TIRAR DADOS)----------------------------------

def tirar_dados(numero_de_dados, cara_inicial, cara_final):
    lista_auxiliar = []
    for i in range(numero_de_dados):
        lista_auxiliar.append(random.randint(cara_inicial, cara_final))

    return lista_auxiliar

    #print(f"Tirada de dados: {lista_auxiliar}")
    #return lista_auxiliar

#-------------------(FUNCIÓN PARA ELEGIR DADOS)-----------------------------------------------------

def elegir_dados(lista_auxiliar):
    
    while True:

        print("\n--- Dados Disponibles ---")
        for i, valor in enumerate(lista_auxiliar):
            print(f"{i + 1}) {valor}")

        entrada = input("Ingrese posiciones a conservar (ej: 1,3,5), o ENTER para no conservar: ")

        if entrada.strip() == "":
            return []

        partes = entrada.split(",")
        dados_elegidos = []
        posiciones_usadas = []

#------------- Ciclio for para comprobar errores ----------
        for p in partes:
            p = p.strip()

            if not p.isdigit():
                print(f"Error: '{p}' no es un número válido.")
                break

            posicion = int(p) - 1

            if posicion < 0 or posicion >= len(lista_auxiliar):
                print(f"Error: La posición {posicion + 1} está fuera del rango.")
                break 

            if posicion in posiciones_usadas:
                print(f"Error: La posición {posicion + 1} ya fue usada.")
                break 

            posiciones_usadas.append(posicion)
            dados_elegidos.append(lista_auxiliar[posicion])
        
        else:

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
        if planilla[cat] != None:
            
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
    
