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

    txt=["*COORDINATES","*ELEMENT_GROUPS","*INCIDENCES",'*GEOMETRIC_PROPERTIES']      
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


        pontos(txt_pontos)
        listabarras=elementos_barra(txt_barra,txt_incidencias,txt_area)  # nessa linha quantidade de elementos barra é dado como return para posterior uso


        for linha in range(len(linhas)):
            linhas[linha]=linhas[linha].replace(","," ")
        return listabar

    def pontos(indice_pontos):

        quantidade_pontos=entrada[indice_pontos+1]

        for linha in range(1,int(quantidade_pontos)+1):
            split=entrada[indice_pontos+linha+1].split()
            dictpontos[int(entrada[indice_pontos+linha+1][0])]=[float(split[1]),float(split[2])]

            
    def elementos_barra(indice_barras,indice_incidencia,indice_area):
        indice_incidencia+=1
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
            indice_incidencia+=1
            indice_area+=1

        



        return listabar

    def incidencias(indice_barra):

        split=entrada[indice_barra].split()
        return [int(split[1]),int(split[2])]
    def area(indice_barra):
    
        split=entrada[indice_barra].split()

        return float(split[0])

    
    
    BAR=check(txt)
    print(BAR)


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
