#pip install firebase

#estos paquetes ayudan en caso de que se presenten problemas con la instalacion de firebase en python

#pip install python_jwt
#pip install gcloud
#pip install pycrypto
#pip install sseclient
#pip install requests-toobelt

from firebase import firebase
import random
from random import randint



class Cuadrangular:

    def calcular(self):
        firebase_handler = firebase.FirebaseApplication("https://pruebaud-25230.firebaseio.com/",None)

        #no se agregan datos de momento
        #resultado=firebase.post('/equipos/datosEquipos',lista)
        #print(type(resultado))

        leer = firebase_handler.get('/equipos/datosEquipos','')
        #convierte el tipo de dato dict a lista
        lista = [ value['nombreEquipo'] for key, value in leer.items() ]
        #nombreEq = random.choice(lista)
        #print("eliminado: ", nombreEq)
        #lista.remove(nombreEq)
        #lista
        #for i in range(len(lista)):
        #print(lista[i])
        tope = 4 
        # +str(i+1)
        # modificar el numero de clubes
        clubes = []
        index_clubes = 0
        for i in range(0, tope):
            nombreEq = random.choice(lista)
            clubes.append(nombreEq)
            lista.remove(nombreEq)
        auxT = len(clubes)
        impar = True if auxT % 2 != 0 else False
        if impar:
            auxT += 1
        totalP = auxT // 2  # total de partidos de una jornada
        jornada = []
        indiceInverso = auxT - 2
        for i in range(1, auxT):
            valoresA = randint(0, 5)
            valoresB = randint(0, 5)
            equipos = []
            list_equipos = {}
            for indiceP in range(0, totalP):
                if index_clubes > auxT - 2:
                    index_clubes = 0
                if indiceInverso < 0:
                    indiceInverso = auxT - 2
                if indiceP == 0:  # seria el partido inicial de cada fecha
                    if impar:
                        equipos.append(clubes[index_clubes])
                    else:
                        if (i + 1) % 2 == 0:
                            partido = [clubes[index_clubes], clubes[auxT - 1]]
                        else:
                            partido = [clubes[auxT - 1], clubes[index_clubes]]
                        equipos.append(" vs ".join(partido))
                        equipos.append('marcador: ' + str(valoresA) + '-' + str(valoresB))
                else:
                    partido = [clubes[index_clubes], clubes[indiceInverso]]
                    equipos.append(" vs ".join(partido))
                    indiceInverso -= 1
                index_clubes += 1
            # print(clubes)
            list_equipos = { 
                'jornada numero: ': str(i),
                'equipos': equipos
            }
            jornada.append(list_equipos)
        jornada
        partidos = firebase_handler.post('/partidos/fechas', jornada)  
        valoresA = randint(0, 5)
        #print(value) 
        len(lista)