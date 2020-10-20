import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def players():
    global currentPlayer
    global new
    global playerCounter
    global dataFrame

    ##Recorre todo el dataframe para los diferentes nombres
    
    for rowNum in range(len(dataFrame)):
        ##Nombre de la fila actual
        name=dataFrame.iloc[rowNum].Nombre+" "+dataFrame.iloc[rowNum].Apellido

        ##Si la fila actual (nombre) es igual a la anterior entonces no lo imprime
        if currentPlayer==name:
            new==False
    
        if currentPlayer!=name:
            new==True
            currentPlayer=name
            print(name)
            playerCounter+=1
        
    print("\nThere are",playerCounter,"players\n\n")


##Funcion para las graficas del jugador
def playerGraph():
    global currentPlayer
    global new
    global playerCounter
    global dataFrame

    print("Que jugador quiere buscar? (Nombre + Apellido)")
    playerName=str(input())
    years=[]
    puntos=[]
    rebounds=[]
    assists=[]
    conferencia=""
    liga=""
    
    ##Se guardan las columnas en las que se encuentra el jugador
    rowsWithPlayer=[]

    found=False

    ##Reiteras la lista para checar si esta el jugador y se guardan en que filas se encuentra
    for rowNum in range(len(dataFrame)):
        name=dataFrame.iloc[rowNum].Nombre+" "+dataFrame.iloc[rowNum].Apellido
        if name==playerName:
            rowsWithPlayer.append(rowNum)
            found=True

            ##Se utilizan estos datos para la grafica
            conferencia=dataFrame.iloc[rowNum].Conferencia
            liga=dataFrame.iloc[rowNum].Liga

    ##Si si se encontro entonces generas la lista
    if found==True:

        ##Guardar los datos del jugador
        for row in rowsWithPlayer:
            years.append(int(dataFrame.iloc[row].Año))
            puntos.append(int(dataFrame.iloc[row].Puntos))
            rebounds.append(int(dataFrame.iloc[row].Rebotes))
            assists.append(int(dataFrame.iloc[row].Asistencias))

        ##Hay mas de una entrada para el jugador
        if len(years)>1:
            years.sort()

            fig1,graficas = plt.subplots(3)
            fig1.suptitle(playerName)
            plt.setp(graficas, xticks=years, xticklabels=years)

            graficas[0].plot(years, puntos,'-go')
            graficas[0].set_title("Puntos")
            

            graficas[1].plot(years, rebounds,'-ro')
            graficas[1].set_title("Rebotes")

            graficas[2].plot(years, assists,'-bo')
            graficas[2].set_title("Asistencias")

            caption=conferencia+" // "+liga
            fig1.text(.5, .05,caption, ha='center')

            plt.show()
        
        ##Solo hay una entrada para el jugador
        else:
            print("Solo se encontro una entrada:\n",dataFrame.iloc[rowsWithPlayer[0]])
    
    else:
        print("No se encontro el jugador\n")
        menu()


##Funcion de menu
def menu():

    print("Que desea hacer?\n<1> Mostrar Jugadores\n<2> Buscar Jugador")
    opcion=int(input())
    print("\n")

    if opcion==1:
        players()
    
    elif opcion==2:
        playerGraph()

    else:
        print("Indique una opcion valida")
        menu()
        exit

##Crear el dataframe
grafica="puntos_jugador.xlsx"
dataFrame=pd.read_excel(grafica)

currentPlayer=""
new=True
playerCounter=0

##Abre el menu
menu()

