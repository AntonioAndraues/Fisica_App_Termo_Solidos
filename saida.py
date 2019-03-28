

dicionario_deslocamento = {1: [30,10], 2: [5,15],3:[20,20]}
dicionario_forcas_reacao = {1: [10,0],2:[40,30]}
dicionario_deformacao_elemento = {1:20,2:20,3:30}
dicionario_elemento_estresse = {1:10,2:10,3:10}

arquivo_saida= open("saida.txt","w+")
pular_linha = "\n"

def saidaDeslocamento(arquivo,dicionario):
	string_inicial = "*DISPLACEMENTS"
	arquivo.write(string_inicial + pular_linha)
	for no in dicionario:
		arquivo.write(str(no) + " ")
		arquivo.write(str(dicionario[no][0]) + " " + str(dicionario[no][1]) + pular_linha)
	arquivo.write(pular_linha)

def saidaForcasReacao(arquivo,dicionario):
	string_inicial = "*REACTION_FORCES"
	arquivo.write(string_inicial + pular_linha)
	for no in dicionario:
		if(dicionario[no][0] != 0):
			arquivo.write(str(no) + " ")
			arquivo.write("FX = " + str(dicionario[no][0])+pular_linha)
		if (dicionario[no][1] != 0):
			arquivo.write(str(no) + " ")
			arquivo.write("FY = " + str(dicionario[no][1]) + pular_linha)
	arquivo.write(pular_linha)

def saidaTensaoElemento(arquivo,dicionario):
	string_inicial = "*ELEMENT_STRAINS"
	arquivo.write(string_inicial + pular_linha)
	for elemento in dicionario:
		arquivo.write(str(elemento) + " ")
		arquivo.write(str(dicionario[elemento]) + pular_linha)
	arquivo.write(pular_linha)

def saidaEstresseElemento(arquivo,dicionario):
	string_inicial = "*ELEMENT_STRESSES"
	arquivo.write(string_inicial + pular_linha)
	for elemento in dicionario:
		arquivo.write(str(elemento) + " ")
		arquivo.write(str(dicionario[elemento]) + pular_linha)
	arquivo.write(pular_linha)


saidaDeslocamento(arquivo_saida,dicionario_deslocamento)
saidaForcasReacao(arquivo_saida,dicionario_forcas_reacao)
saidaTensaoElemento(arquivo_saida,dicionario_deformacao_elemento)
saidaEstresseElemento(arquivo_saida,dicionario_elemento_estresse)
arquivo_saida.close()







