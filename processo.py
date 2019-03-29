# -*- coding: utf-8 -*-
import numpy as np
from matriz import main
from metNum import resolve_jacobi
from saida import *

BAR,NOS,LOADS = main()

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

def cria_rigidez(listabarras): #numero elemento é 1, 2 , 3 etc
	n = len(NOS)
	matriz_rigidez_global = np.zeros((2*n,2*n))
	for barra in listabarras:
		incidencias = barra["incidencia"]
		# print(incidencias)
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
	return matriz_rigidez_global


def aplica_restricao(lista,matriz_global):
	matriz_restricao = []
	linha=0
	coluna=0
	n=(len(lista))
	# print(lista)
	matriz_restricao = np.zeros((n,n))
	# print(len(matriz_restricao))
	for j in range(len(matriz_global)):
		for i in range(len(matriz_global)):
			if (j in lista and i in lista):
				matriz_restricao[linha][coluna]=matriz_global[i][j]
				coluna+=1
				if(coluna>=len(lista)):
					linha+=1
					coluna=0
	return matriz_restricao	

def loads(nos,loads,lista):
	matriz_PG= np.zeros((2*len(nos),1))
	matriz_array=np.zeros((len(lista),1))
	for no in nos:
		try:	
			matriz_PG[no*2-2][0]=loads[str(no)][0]
			matriz_PG[no*2-1][0]=loads[str(no)][1]

		except:
			pass
	for i in range(len(lista)):
		matriz_array[i][0]=matriz_PG[lista[i]][0]
	return matriz_array
		
def bcnodes(nos):
	lista_nos_livres = []

	for no in nos:
		lista_restricoes = nos[no][2:]
		while len(lista_restricoes) <=1:
			lista_restricoes.append(0)
		for i in range(len(lista_restricoes)):
			lista_restricoes[i]=int(lista_restricoes[i])
		if lista_restricoes[0]==2:
			lista_restricoes.sort()
		for i in lista_restricoes:
			if i == 1:
				lista_nos_livres.append(1)
			if i == 2:
				lista_nos_livres.append(1)
			if i==0:
				lista_nos_livres.append(0)

	lista_liberdade =[]
	for contador in range(len(lista_nos_livres)):
		if lista_nos_livres[contador] == 0:
			lista_liberdade.append(contador)
	return lista_liberdade,lista_nos_livres


def tensao(barras, jacobi):
	a=1
	dicionario_tensao = {}
	for barra in barras:
		matriz_s_c = [[-barra['c'],-barra['s'],barra['c'],barra['s']]]
		matriz_desloc = ([[jacobi[barra['incidencia'][0]][0]],[jacobi[barra['incidencia'][0]][1]],[jacobi[barra['incidencia'][1]][0]],[jacobi[barra['incidencia'][1]][1]]])
		mult_matriz = (np.dot(matriz_s_c,matriz_desloc)[0][0])
		tensao = (barra['materiais'][0]/barra['l'])*mult_matriz
		dicionario_tensao[a]=tensao
		a+=1
	return dicionario_tensao

def deformacao(barras, jacobi):
	a=1
	dicionario_deformacao = {}
	for barra in barras:
		matriz_s_c = [[-barra['c'],-barra['s'],barra['c'],barra['s']]]
		matriz_desloc = ([[jacobi[barra['incidencia'][0]][0]],[jacobi[barra['incidencia'][0]][1]],[jacobi[barra['incidencia'][1]][0]],[jacobi[barra['incidencia'][1]][1]]])
		mult_matriz = (np.dot(matriz_s_c,matriz_desloc)[0][0])
		tensao = (1/barra['l'])*mult_matriz
		dicionario_deformacao[a]=tensao
		a+=1
	return dicionario_deformacao

def forcasResultantes(matriz_global,jacobi,lista_nos_livres):
	lista_deslocamento = []


	for i in jacobi:
		lista_deslocamento.append(jacobi[i][0])
		lista_deslocamento.append(jacobi[i][1])


	matriz=np.zeros((len(lista_deslocamento),1))

	for i in range(len(lista_deslocamento)):
		matriz[i][0]=lista_deslocamento[i]

	matriz_forcas = np.dot(matriz_global,matriz)
	lista_temp=[]
	for item in matriz_forcas:
		lista_temp.append(item[0])

	lista_presos = []
	for contador in range(len(lista_nos_livres)):
		if lista_nos_livres[contador] == 1:
			lista_presos.append(lista_temp[contador])
		if lista_nos_livres[contador] == 0:
			lista_presos.append(0)

	return lista_presos




lista_liberdade,lista_nos_livres = bcnodes(NOS)
lista_n = calcula_lsc(BAR,NOS)
matriz_global = cria_rigidez(lista_n)
matriz_restricao=aplica_restricao(lista_liberdade, matriz_global)
matriz_array=loads(NOS,LOADS,lista_liberdade)


#######################    TESTE JACOB    ###############################
it = int(input("Qual o número de interações?"))
tol = float(input("Qual a tolerância? "))
l_global = len(matriz_global)
U_jacobi, erro_jacobi,itJacobi = resolve_jacobi(l_global,matriz_restricao, matriz_array, it, tol,lista_liberdade)

print(U_jacobi)
dicionario_deslocamento = U_jacobi
dicionario_elemento_deformacao = deformacao(BAR,U_jacobi)
dicionario_elemento_tensao = tensao(BAR,U_jacobi)
lista_reacoes = forcasResultantes(matriz_global,U_jacobi,lista_nos_livres)



arquivo_saida= open("saida.txt","w+")

saidaDeslocamento(arquivo_saida,dicionario_deslocamento)
saidaForcasReacao(arquivo_saida,lista_reacoes)
saidaDeformacaoElemento(arquivo_saida,dicionario_elemento_deformacao)
saidaTensaoElemento(arquivo_saida,dicionario_elemento_tensao)
# print("Erro jacobi: ", erro_jacobi)
# print("Iterações necessárias jacobi: ", itJacobi)



# it = int(input("Qual o número de interações?"))
# tol = float(input("Qual a tolerância? "))
# U_gauss, erro_gauss,itGauss = resolve_gauss(rigidez, forca, it, tol)
# U_jacobi, erro_jacobi,itJacobi = resolve_jacobi(rigidez, forca, it, tol)

# print("U gauss: ", U_gauss)
# print("Erro gauss: ",erro_gauss)
# print("Iterações necessárias gauss: ", itGauss)

# print("U jacobi: ", U_jacobi)
# print("Erro jacobi: ", erro_jacobi)
# print("Iterações necessárias jacobi: ", itJacobi)


