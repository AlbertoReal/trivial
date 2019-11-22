#program principal principal

facil = [["facil","pregunta facil","a","b","c",2],["clase","p1","a","b","c",2]]
normal= [["normal","pregunta normal","a","b","c",2],["clase","p1","a","b","c",2]]
dificil = [["dificil","pregunta dificil","a","b","c",2],["clase","p1","a","b","c",2]]


jugador1 =[[0,0,False],[0]]
jugador2 =[[0,0,False],[0]]
jugador3 =[[0,0,False],[0]]
jugador4 =[[0,0,False],[0]]
jugador5 =[[0,0,False],[0]]
jugador6 =[[0,0,False],[0]]


turno=0
jugador_eleccion = [0]


#funcion

def juego (turno,jugadores_totales):
        
        while turno<jugadores_totales*10:               
                salir=False

                while salir==False:
                        entrada=int(input("nivel de dificultad facil opcion 1, normal opcion2 o dificil opcion 3 elije y escribe una "))
                        if entrada ==1 or entrada ==2 or entrada ==3:
                                salir=True
                        else:
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

                if entrada ==1:
                        jugador[0][2]=facil
                elif entrada ==2:
                        jugador[0][2]=normal
                else: 
                        jugador[0][2]=dificil

                     
                tirada_dado = 0
                pregunta =jugador[0][2]
                puntos=0
                racha=0
                
                print ("La pregunta es de: ",pregunta[0][0])
                print ("pregunta ",pregunta[0][1])
                print ("respuesta A ",pregunta[0][2])
                print ("respuesta B ",pregunta[0][3])
                print ("respuesta C ",pregunta[0][4])

                rachas = jugador[1][0]

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

                if jugador[1][0] >2:
                        jugador[1][0]=0


                puntos_base=jugador[0][0]
                puntos_totales=puntos_base + puntos
                racha_base=jugador[1][0]
                racha_total=racha + racha_base

                jugador[0][0] = puntos_totales
                jugador[1][0] = racha_total


                #print para ver su funcionamiento

                #return para guardar el turno que se juega
                #return turno

                print (jugador[0][0])
                print (jugador[1][0])
        total_jugador1=jugador1[0][0]
        total_jugador2=jugador2[0][0]
        print(jugador_eleccion[0])

        if total_jugador1>total_jugador2:
                print ("jugador 1 a ganado con ",total_jugador1)
                print(turno)
        elif total_jugador1 < total_jugador2:
                print ("jugador 2 a ganado con ",total_jugador2)
                print(turno)
        else:
                print ("empate")
                print(turno)
#programa principal    

jugadores2 = int(input("numero de jugadores entre 2 y 6 "))
juego(turno,jugadores2)

