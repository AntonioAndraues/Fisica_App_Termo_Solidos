import numpy as np
def main():
    fname='entrada.txt'
    with open (fname, 'rt') as file:
        entrada =file.read().strip().split()
    linhas=[]
    dictpontos={}
    dictBAR={}

    txt=["*COORDINATES","*ELEMENT_GROUPS"]
    def check(fname, txt):





        for lines in range(len(entrada)):
            entrada[lines]=entrada[lines].replace(","," ")
            if entrada[lines] in txt[0]:
                txt_pontos=lines
            if entrada[lines] in txt[1]:
                txt_barra=lines


        pontos(txt_pontos)
        elementos_barra(txt_barra)


        # print(linhas)
        for i in range(len(linhas)):
            linhas[i]=linhas[i].replace(","," ")
    def pontos(i):

        quantidade_pontos=entrada[i+1]

        for j in range(1,int(quantidade_pontos)+1):
            # print(entrada[i+j+1].split())
            # print(entrada[i+j+1])
            split=entrada[i+j+1].split()
            dictpontos[int(entrada[i+j+1][0])]=[float(split[1]),float(split[2])]
            print(dictpontos)
    def elementos_barra(i):

        quantidade_pontos=entrada[i+1]
        print(entrada)
        for j in range(1,int(quantidade_pontos)+1):
            # print(entrada[i+j+1].split())
            # print(entrada[i+j+1])
            split=entrada[i+j+1].split()
            dictBAR[int(entrada[i+j+1][0])]=[float(split[1]),(split[2])]
            print(dictBAR)


    string="*COORDINATES"
    entrada=check('entrada.txt', txt)
    # pontos(linhas,dictpontos)
    # print(dictpontos[1])




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
