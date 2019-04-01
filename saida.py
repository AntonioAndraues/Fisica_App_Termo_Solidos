arquivo_saida= open("saida.txt","w+")
pular_linha = "\n"

def saidaDeslocamento(arquivo,dicionario):
	string_inicial = "*DISPLACEMENTS"
	arquivo.write(string_inicial + pular_linha)
	for no in dicionario:
		arquivo.write(str(no) + " ")
		arquivo.write(str(dicionario[no][0]) + " " + str(dicionario[no][1]) + pular_linha)
	arquivo.write(pular_linha)

def saidaForcasReacao(arquivo,lista):
	string_inicial = "*REACTION_FORCES"
	arquivo.write(string_inicial + pular_linha)
	a = 0
	b = 1
	n = int(len(lista)/2)
	for contador in range(n):
		if lista[a] == 0:
			a = a + 2
		else:
			arquivo.write(str(contador+1) + " FX = " + str(lista[a]) + pular_linha)
			a = a +2
		if lista[b] == 0:
			b = b + 2
		else:
			arquivo.write(str(contador+1) + " FY = " + str(lista[b]) + pular_linha)
			b = b + 2
	arquivo.write(pular_linha)

def saidaDeformacaoElemento(arquivo,dicionario):
	string_inicial = "*ELEMENT_STRAINS"
	arquivo.write(string_inicial + pular_linha)
	for elemento in dicionario:
		arquivo.write(str(elemento) + " ")
		arquivo.write(str(dicionario[elemento]) + pular_linha)
	arquivo.write(pular_linha)

def saidaTensaoElemento(arquivo,dicionario):
	string_inicial = "*ELEMENT_STRESSES"
	arquivo.write(string_inicial + pular_linha)
	for elemento in dicionario:
		arquivo.write(str(elemento) + " ")
		arquivo.write(str(dicionario[elemento]) + pular_linha)
	arquivo.write(pular_linha)



arquivo_saida.close()







