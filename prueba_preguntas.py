#program principal principal

facil = [["facil","pregunta facil","a","b","c",2],["clase","p1","a","b","c",2]]
normal= [["normal","pregunta normal","a","b","c",2],["clase","p1","a","b","c",2]]
dificil = [["dificil","pregunta dificil","a","b","c",2],["clase","p1","a","b","c",2]]

jugador1 = [[0,0,False,1],[0]]
jugador2 = [[0,0,False,2],[0]]
jugador3 = [[0,0,False,3],[0]]
jugador4 = [[0,0,False,4],[0]]
jugador5 = [[0,0,False,5],[0]]
jugador6 = [[0,0,False,6],[0]]

puntuacion =[]
turno=0
jugador_eleccion = [-1]

import random
from time import sleep
import os

def temporizadorTrivial():
#temporizador 10 segundos, 10 a 0
        time=True
        for i in range(0,10):
                print(10 -i)
                sleep(1)
                os.system ("cls")
                salida=(10-i)
        time=False
        return time



def mostrarMenu():
        print("=============================")
        print("=                     M E N U                         =")
        print("=============================")
        print("1) Jugar")
        print("2) Salir")
    
        salir = True
        while salir==True:
                print("Iniciando juego")
                menu = input("Dime que opción deseas: ")
                if menu == "1":
                        jugadores_validos = True
                        while jugadores_validos == True:
                                jugadores=input("cuantos jugadores van a participar: ")
                                if (jugadores=="2" or jugadores=="3" 
                                or jugadores=="4" or jugadores=="5" or jugadores=="6"):
                                        jugadores=int(jugadores)
                                        juego(turno,jugadores)
                                else:
                                        jugadores=input("cuantos jugadores van a participar: ")
                                        
                       
                elif menu == "2":
                        salir = False
                        jugadores_validos = False
                        print("Salir")
                        print(salir)



def dado():        
        dado=(random.randrange(50))
        return dado

def resetearPuntuacion():
        jugador1[0][0]=0
        jugador2[0][0]=0
        jugador3[0][0]=0
        jugador4[0][0]=0
        jugador5[0][0]=0
        jugador6[0][0]=0
        

def juego (turno,jugadores_totales):
        
        while turno<jugadores_totales*5:               
                salir=False

                if jugador_eleccion[0]<jugadores_totales-1:
                        jugador_eleccion[0]+=1
                else:
                        jugador_eleccion[0]=0
                if jugador_eleccion[0]==0:
                        jugador=jugador1                                
                        turno+=1
                        
                elif jugador_eleccion[0]==1:
                        jugador=jugador2
                        turno+=1
                                
                elif jugador_eleccion[0]==2:
                        jugador=jugador3
                        turno+=1
                                
                elif jugador_eleccion[0]==3:
                        jugador=jugador4
                        turno+=1
                                
                elif jugador_eleccion[0]==4:
                        jugador=jugador5
                        turno+=1
                                
                elif jugador_eleccion[0]==5:
                        jugador=jugador6
                        
                while salir==False:                        
                        if jugador[0][2]==False:                                
                                entrada=input("nivel de dificultad facil opcion 1, normal opcion2 o\n dificil opcion 3 elije y escribe una ")                              
                                if entrada =="1" or entrada =="2" or entrada =="3":
                                        entrada=int(entrada)
                                        if entrada ==1:
                                                jugador[0][2]=facil
                                        elif entrada ==2:
                                                jugador[0][2]=normal
                                        else: 
                                                jugador[0][2]=dificil
                                        salir=True
                        else:
                                salir=True
                
                tope_preguntas = len(jugador[1])
                
                tirada_dado=dado()
                
                for i in range (tope_preguntas-1):
                        if jugador[1][i] == tirada_dado:
                                tirada_dado=dado()
             
                pregunta = jugador[0][2]
                puntos=0
                racha=0
                print ("\n")
                print ("*****jugador" ,jugador[0][3],"es tu turno*****\n")
                print ("La pregunta es de: ",pregunta[0][0])
                print (pregunta[0][1])
                print ("\n")
                print (pregunta[0][2])
                print (pregunta[0][3])
                print (pregunta[0][4])
                print ("\n")

                rachas = jugador[1][0]                
                respuesta = input("respuesta ")                
                respuesta_valida =False
               
                while respuesta_valida == False:
                        if respuesta =="1" or respuesta =="2" or respuesta =="3":
                                respuesta=int(respuesta)
                                respuesta_valida=True
                        else:
                                print("respuesta imposible vuelve a probar")
                                respuesta = input("respuesta ")

                if respuesta == pregunta[0][5]:

                    if pregunta == facil:
                        if rachas >2:
                            puntos = 6
                        else:
                            puntos=3
                            racha=1
                    elif pregunta == normal:
                        if rachas >2:
                            puntos=12
                        else:
                            puntos=6
                            racha=1
                    else:
                        if racha>2:
                            puntos=18
                        else:
                            puntos=9
                            racha=1
                else:
                    puntos=0
                    racha=0
                    print("respuesta no valida")

                puntos_base=jugador[0][0]
                puntos_totales=puntos_base + puntos
                racha_base=jugador[1][0]
                racha_total=racha + racha_base

                jugador[0][0] = puntos_totales
                jugador[0][1] = racha_total
                jugador[1].append(tirada_dado)
                print(jugador[0][0])
                                
        if turno>=jugadores_totales*5:
                puntuacion=[]
                puntuacion.append(jugador1[0][0])
                puntuacion.append(jugador2[0][0])
                puntuacion.append(jugador3[0][0])
                puntuacion.append(jugador4[0][0])
                puntuacion.append(jugador5[0][0])
                puntuacion.append(jugador6[0][0])
         

        tope=len(puntuacion)
        maximo=0
        for i in range (tope):               
                if puntuacion[i]>maximo:
                        maximo=puntuacion[i]
                        tope_total=i
                                                        
        print ("jugador",tope_total+1,"es el ganador con",maximo,"puntos \n")
        resetearPuntuacion()
        mostrarMenu()
                                                
mostrarMenu()

