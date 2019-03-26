# -*- coding: utf-8 -*-
import numpy as np
from matriz import main

BAR,NOS = main()

"""
*COORDINATES
3
1 0 0
2 0 0.4
3 0.3 0.4

*ELEMENT_GROUPS
3
1 1 BAR
2 1 BAR
3 1 BAR

*INCIDENCES
1 1 2
2 2 3
3 3 1

*MATERIALS
3
210E9 1570E6 1570E6
210E9 1570E6 1570E6
210E9 1570E6 1570E6

*GEOMETRIC_PROPERTIES
3
2E-4
2E-4
2E-4 

*BCNODES
3
1 1
2 1
2 2

*LOADS
2
3 1 150
3 2 -100
"""


def cria_elementos(dict_coordenadas, dict_incidences): #retorna um dic com os pontos de cada barra
    dict_elementos = {}
    k=1
    for incidencia in dict_incidences: #pego as incidencias de cada barra e depois as coordenadas destas incidencias
        l_p1 = []
        l_p2 = []
        p1 = dict_incidences[incidencia][0]
        p2 = dict_incidences[incidencia][1]
        x1 = dict_coordenadas[p1][0]
        y1 = dict_coordenadas[p1][1]
        x2 = dict_coordenadas[p2][0]
        y2 = dict_coordenadas[p2][1]
        l_p1.append(x1)
        l_p1.append(y1)
        l_p2.append(x2)
        l_p2.append(y2)
        dict_elementos.update({k:l_p1+l_p2})
        k+=1
    return dict_elementos
    
        
def calcula_lsc(listabarras, dict_nos):
    for barra in listabarras:
        incidencias = barra["incidencia"]
        coordenadas_1 = (dict_nos[incidencias[0]][:2])
        coordenadas_2 = (dict_nos[incidencias[1]][:2])
        print(coordenadas_1)
        print(coordenadas_2)
        x1 = float(coordenadas_1[0])
        y1 = float(coordenadas_1[1])
        x2 = float(coordenadas_2[0])
        y2= float(coordenadas_2[1])

        L = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
        cosseno = (x2-x1)/L
        seno = (y2-y1)/L
        barra["l"] = L
        barra["s"] = seno
        barra["c"]=cosseno
        return listabarras
#calcula_lsc(BAR,NOS)

def cria_rigidez(dict_lsc, dict_materiais, numero_elemento): #numero elemento é 1, 2 , 3 etc
    # n = len(dict_lsc) #para pegar o numero de elementos
    # matriz = np.zeros((n,n)) #criando uma matriz com zeros para preencher depois
    # eal = dict_materiais[numero_elemento]
    # j = 0 
    # for i in range(n-1):
    #     matriz[i][j] = (dict_lsc[numero_elemento][2]**2)

    return 0


dict_coordenadas = {1: [0.0, 0.0], 2: [0.0, 0.4], 3: [0.3, 0.4]} 
dict_incidences =  {1: [1, 2], 2: [2, 3], 3: [3, 1]}

dict_elementos = cria_elementos(dict_coordenadas, dict_incidences)

# dict_lsc = calcula_lsc(dict_elementos)

# dict_barras = {1: [1,2,2*10**(-4),0,0], 2: [2,3,2*10**(-4),0,0]], 3: [3,1,2*10**(-4),0,0]}

