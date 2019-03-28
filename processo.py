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
        
def calcula_lsc(listabarras, dict_nos):
	for barra in listabarras:

		incidencias = barra["incidencia"]
		coordenadas_1 = (dict_nos[incidencias[0]][:2])
		coordenadas_2 = (dict_nos[incidencias[1]][:2])
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
# lista_n = calcula_lsc(BAR,NOS)
# print(lista_n)

def cria_rigidez(listabarras): #numero elemento é 1, 2 , 3 etc
	n = len(listabarras)
	matriz_rigidez_global = np.zeros((2*n,2*n))
	for barra in listabarras:
		incidencias = barra["incidencia"]
		print(incidencias)
		b=2*incidencias[0]-1 #matriz global começa em 0 nao em 1
		a=b-1
		d=2*incidencias[1]-1
		c=d-1
		E = barra["materiais"][0]	
		area = barra["area"]
		l = barra["l"]
		if(l == 0):
			Eal = 0
		else:
			Eal = E*area*(1/l)
		cos = barra["c"]
		s = barra["s"]
		matriz_cs = [[Eal * cos**2,Eal * cos*s,Eal * -cos**2,Eal * -cos*s], 
		[Eal *cos*s,Eal * s**2,Eal * -cos*s,Eal * -s**2],
		[Eal *-cos**2,Eal * -cos*s,Eal * cos**2,Eal * cos*s],
		[Eal *-cos*s,Eal * -s**2,Eal * cos*s,Eal * s**2]]

		matriz_rigidez_global[a][a] += matriz_cs[0][0]
		matriz_rigidez_global[a][b] += matriz_cs[0][1]
		matriz_rigidez_global[a][c] += matriz_cs[0][2]
		matriz_rigidez_global[a][d] += matriz_cs[0][3]
		matriz_rigidez_global[b][a] += matriz_cs[1][0]
		matriz_rigidez_global[b][b] += matriz_cs[1][1]
		matriz_rigidez_global[b][c] += matriz_cs[1][2]
		matriz_rigidez_global[b][d] += matriz_cs[1][3]
		matriz_rigidez_global[c][a] += matriz_cs[2][0]
		matriz_rigidez_global[c][b] += matriz_cs[2][1]
		matriz_rigidez_global[c][c] += matriz_cs[2][2]
		matriz_rigidez_global[c][d] += matriz_cs[2][3]
		matriz_rigidez_global[d][a] += matriz_cs[3][0]
		matriz_rigidez_global[d][b] += matriz_cs[3][1]
		matriz_rigidez_global[d][c] += matriz_cs[3][2]
		matriz_rigidez_global[d][d] += matriz_cs[3][3]

		#print(matriz_rigidez_global)
	return matriz_rigidez_global

lista_n = calcula_lsc(BAR,NOS)
matriz_global = cria_rigidez(lista_n)



