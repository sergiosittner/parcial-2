#----------------------------------(FUNCION ANOTAR NOMBRE Y PUNTOS EN CSV)----------------------------
def guardar_puntaje(nombre, puntos):
    with open("estadisticas.csv", "a") as archivo:
        archivo.write(f"{nombre},{puntos}\n") 
    print("\nPuntaje guardado correctamente.")

#---------------------------------------(LEER NOMBRES Y PUNTOS DEL ARCHIVO CSV)---------------------------

def estadisticas():
    print("\n======= TABLA DE POSICIONES =======")
    lista_jugadores = []
    

    with open("estadisticas.csv", "r") as archivo:
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

    contador = 1
    for nombre, puntos in lista_jugadores[:10]:
        print(f"{contador}°. {nombre:<15} | {puntos} puntos")
        contador += 1


    print("===========================================\n")