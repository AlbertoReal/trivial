#program principal principal

facil = [["facil","pregunta facil","a","b","c",2],["clase","p1","a","b","c",2]]
normal= [["ciencia","de color","rojo","verde","azul",2],["clase","p1","a","b","c",2]]
dificil = [["dificil","pregunta dificil","a","b","c",2],["clase","p1","a","b","c",2]]


jugador1 = [[0,0,False,1],[0]]
jugador2 = [[0,0,False,2],[0]]
jugador3 = [[0,0,False,3],[0]]
jugador4 = [[0,0,False,4],[0]]
jugador5 = [[0,0,False,5],[0]]
jugador6 = [[0,0,False,6],[0]]

turno=0
jugador_eleccion = [-1]

#funcion
#arreglar elegir ganador entre todos los jugadores guaradar al terminar turnos la puntuacion en una lista
#recorrer y buscar cuel es el mayor su posicion +1 es el jugador ganador
#arreglar si acierta tengo otra pregunta del mismo tipo



import random

def dado():
        
        dado=(random.randrange(50))
        return dado


def juego (turno,jugadores_totales):
        
        while turno<jugadores_totales*10:               
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
                                entrada=int(input("nivel de dificultad facil opcion 1, normal opcion2 o dificil opcion 3 elije y escribe una "))                               
                                if entrada ==1 or entrada ==2 or entrada ==3:
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
                for i in range (tope_preguntas-1):
                        if jugador[1][i] == tirada_dado:
                                tirada_dado=dado()
                                                              
                pregunta = jugador[0][2]
                puntos=0
                racha=0
                print ("\n")
                print ("jugador" ,jugador[0][3],"es tu turno\n")
                print ("La pregunta es de: ",pregunta[0][0])
                print ("pregunta ",pregunta[0][1])
                print ("\n")
                print ("respuesta A ",pregunta[0][2])
                print ("respuesta B ",pregunta[0][3])
                print ("respuesta C ",pregunta[0][4])
                print ("\n")

                rachas = jugador[1][0]
                
                respuesta = int(input("respuesta "))
                
                respuesta_valida =False
                
                while respuesta_valida == False:
                        if respuesta ==1 or respuesta ==2 or respuesta ==3:
                                respuesta_valida=True
                        else:
                                print("respuesta imposible vuelve a probar")
                                respuesta = int(input("respuesta "))

                        

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
                jugador[1][0] = racha_total
                
                if jugador[1][0]==1:
                        jugador_acierta=True
                elif jugador[1][0]>1:
                        ejugador_acierta=False


                #print para ver su funcionamiento
                
                #return para guardar el turno que se juega
                #return turno

                print (jugador[0][0])
        

        if total_jugador1>total_jugador2:
                print ("jugador 1 a ganado con ",total_jugador1)
                print(turno)
        elif total_jugador1 < total_jugador2:
                print ("jugador 2 a ganado con ",total_jugador2)
                print(turno)
        else:
                print ("empate ","jugador 1 con",total_jugador)
                print(turno)
                
#programa principal    

jugadores2 = int(input("numero de jugadores entre 2 y 6 "))
juego(turno,jugadores2)

