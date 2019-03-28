# -*- coding: utf-8 -*-
import numpy as np
def main():
    fname='entrada.txt'
    with open (fname, 'rt') as file:
        entrada =file.read().strip().split()
    linhas=[]
    quantidade_barra=0
    dictpontos={}
    listabar=[]
    dictIncidencia={}
    dictloads={}

    txt=["*COORDINATES","*ELEMENT_GROUPS","*INCIDENCES",'*GEOMETRIC_PROPERTIES','*LOADS','*MATERIALS','*BCNODES']      

    def check(txt):

        for lines in range(len(entrada)):
            entrada[lines]=entrada[lines].replace(","," ")
            if entrada[lines] in txt[0]:
                txt_pontos=lines
            if entrada[lines] in txt[1]:
                txt_barra=lines
            if entrada[lines] in txt[2]:
                txt_incidencias=lines
            if entrada[lines] in txt[3]:
                txt_area=lines
            if entrada[lines] in txt[4]:
                txt_loads=lines
            if entrada[lines] in txt[5]:
                txt_materials=lines
            if entrada[lines] in txt[6]:
                txt_bcnodes=lines


        lista=pontos(txt_pontos,txt_bcnodes)
        #print(lista)
        loads(txt_loads)
        listabarras=elementos_barra(txt_barra,txt_incidencias,txt_area,txt_materials)  # nessa linha quantidade de elementos barra é dado como return para posterior uso

        for linha in range(len(linhas)):
            linhas[linha]=linhas[linha].replace(","," ")
        return listabarras,lista
    def pontos(indice_pontos,indice_bcnodes):

        quantidade_pontos=entrada[indice_pontos+1]
        quantidade_bcnodes=entrada[indice_bcnodes+1]
        lista=[]
        dicionario_pontos={}
        for linhas in range(1,int(quantidade_bcnodes)+1):
            split2=entrada[indice_bcnodes+linhas+1].split()
            lista.append(split2)
        
        lista2=[]    
        for linha in range(1,int(quantidade_pontos)+1):
            split=entrada[indice_pontos+linha+1].split()
            temp=0
            lista2.append(split)
        # print(lista2)
        for linha in range(1,int(quantidade_bcnodes)+1):
            # print(entrada[indice_bcnodes+linha+1].split()[0])
            
            for i in range(len(lista2)):
                if (lista2[i][0] == entrada[indice_bcnodes+linha+1].split()[0]):
                    # print(entrada[indice_bcnodes+linha+1].split()[1])
                    lista2[i].append(entrada[indice_bcnodes+linha+1].split()[1])

        # print(lista2)


        for item in lista2:
            dicionario_pontos[int(item[0])] = item[1:]



        return (dicionario_pontos)


    
    
    def loads(indice_loads):
        
        quantidade_load=entrada[indice_loads+1]
        # print(quantidade_load)
        lista_loads=[0,0]
        for linha in range(1,int(quantidade_load)+1):
            # print(entrada[indice_loads+linha+1].split())
            split=entrada[indice_loads+linha+1].split()
            if(int(split[1])==1):
                lista_loads[0]=split[2]
                lista_loads[1]=0
                temp=0
            if(int(split[1])==2):
                lista_loads[1]=split[2]
                temp=1
            dictloads[entrada[indice_loads+linha+1][0]]=[lista_loads[0],lista_loads[1]]
            if(temp):
                lista_loads=[0,0]

    def elementos_barra(indice_barras,indice_incidencia,indice_area,incide_materiais):
        indice_incidencia+=1
        incide_materiais+=2
        indice_area+=2
        quantidade_barra=entrada[indice_barras+1]
        for i in range(1,int(quantidade_barra)+1):
            a="dicionario{0}".format(i)
            a={}
            listabar.append(a)
        for i in range(0,int(quantidade_barra)):
            b=listabar[i]
            b['incidencia']=incidencias(indice_incidencia)
            b['l']=0
            b['area']=area(indice_area)
            b['c'] = 0
            b['s'] = 0
            b['materiais']=materiais(incide_materiais,quantidade_barra)
            indice_incidencia+=1
            indice_area+=1

        # print(listabar)
        return listabar

    def incidencias(indice_barra):

        split=entrada[indice_barra].split()
        return [int(split[1]),int(split[2])]
    def materiais(indice_materiais,quantidade_barra):
        split=entrada[indice_materiais].split()

        return[float(split[0]),float(split[1]),float(split[2])]
        
    def area(indice_barra):
    
        split=entrada[indice_barra].split()

        return float(split[0])

    BAR,NOS = check(txt)
    return BAR,NOS
    
    ##print(BAR)
    #print(dictloads)
    #print(dictpontos)


    # print(dictpontos)
    # print(dictBAR)
    # print(dictIncidencia)




    EA_l = 2*(10**9)
    u1=0
    F2=50000
    M_M = np.array([[EA_l,-EA_l],[-EA_l,EA_l]])
    u2=F2/M_M[1][1]
    F1=u2*M_M[0][1]
    M_D= np.matrix([[u1],[u2]])
    M_R=np.matrix([[F1],[F2]])
    M_IR=np.matrix([["F1"],["F2"]])
    # print("Matriz resposta :\n {0}\n =\n {1}".format(M_IR,M_D))
    # print("Matriz resposta :\n {0}\n = \n {1}\n * \n {2}".format(M_R,M_M,M_D))

# --------------------------------
if __name__ == '__main__':

    main()
