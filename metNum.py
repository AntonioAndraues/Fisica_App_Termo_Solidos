# -- coding: UTF-8 --
import numpy as np
import copy
def resolve_gauss(n_nos,rigidez, forca, it, tol,BCNodes):
    n=int(n_nos/2)
    nr=len(rigidez)

    U = np.zeros((nr,1))
    i = 0
    itera=0
    l_erro = []
    while (i<it):
        l_erro = []
        U_anterior = copy.copy(U)

        for j in range(nr):
            U[j] = forca[j]
            #ANTERIOR
            for k in range(nr):
                if k>j:
                    U[j]-=(rigidez[j,k]*U_anterior[k])


            #ATUAL
            for l in range(j):
                if (l)<j:
                    U[j]-=rigidez[j,l]*U[l]

            U[j]=U[j]/rigidez[j,j]



            if(U[j] == 0):  
                erro = 1
            else:
                erro = abs((U[j] - U_anterior[j])/U[j])
            l_erro.append(erro) 
        i+=1
        if max(l_erro)<tol:
            itera=i
            break  

    print("   ")
    print("   ")
    print("Numero de iterações:")
    print(itera)
    print("   ")
    print("   ")
    print("U:")


    #Coloca os 0s no U
    Listaresp=[]
    l=0
    for k in range(2*n):
        if (k) in BCNodes:
            Listaresp.append(U[l])
            l+=1 
        else:
            Listaresp.append(0)
    
    #Coloca os valores no dicionario
    DicResp ={}
    No=0
    for D in range(n):
        DicResp[D+1]=[float(Listaresp[No]),float(Listaresp[No+1])]
        No+=2
    return DicResp,max(l_erro),itera


def resolve_jacobi(n_nos,rigidez, forca, it, tol,BCNodes):
    n=int(n_nos/2)
    nr=len(rigidez)
    #print("DET")
    # print(np.linalg.det(rigidez))
    print(BCNodes)
    U = np.zeros((nr,1))
    i = 0
    itera=0
    l_erro = []
    #lambida para o método de auxilio aconvergencia
    lamb=0.5
    while (i<it):
        l_erro = []
        
        U_anterior= copy.copy(U)
        # print("COPY")
        # print(U_anterior)
        for j in range(nr):

            
            U[j] = forca[j]
            for k in range(nr):
                if k!=j:
                    U[j]-=(rigidez[j,k]*U_anterior[k])
                    #print(j,k)
            U[j]=U[j]/rigidez[j,j]

            #metodo de auxilio convergencia
            U[j]=U_anterior[j]*lamb + U[j]*(1-lamb)



            #print(U[j])
            if(U[j] == 0):
                erro = 1
            else:
                erro = abs((U[j] - U_anterior[j])/U[j])
            l_erro.append(erro) 
        i+=1
        if max(l_erro)<tol:
            itera=i
            break  

    #METODO POR MULTIPLICAÇÃo PELA INVERSA ESTA FUNCIONADO
    # U=np.matmul( np.linalg.inv(rigidez),forca)

    print(itera)
    Listaresp=[]
    l=0
    for k in range(2*n):
        if (k) in BCNodes:
            Listaresp.append(U[l])
            l+=1 
        else:
            Listaresp.append(0)

    DicResp ={}
    No=0
    for D in range(n):
        DicResp[D+1]=[float(Listaresp[No]),float(Listaresp[No+1])]
        No+=2
    return DicResp,(l_erro),itera






# rigidez = 10**8*np.array([[1.59,-0.4, -0.54],[-0.4,1.7, 0.4], [-0.54, 0.4, 0.54]])

# forca = np.array([[0],[150], [-100]])

# BCNodes=[2,5,6]


# it = int(input("Qual o número de interações?"))
# tol = float(input("Qual a tolerância? "))



#######################    TESTE JACOB    ###############################

# U_jacobi, erro_jacobi,itJacobi = resolve_jacobi(rigidez, forca, it, tol,BCNodes)
# print("U jacobi: ", U_jacobi)
# print("Erro jacobi: ", erro_jacobi)
# print("Iterações necessárias jacobi: ", itJacobi)




#######################   TESTE GAUS    ##############################
# U_gauss, erro_gauss,itGauss = resolve_jacobi(rigidez, forca, it, tol,BCNodes)
# print("U gauss: ", U_gauss)
# print("Erro gauss: ",erro_gauss)
# print("Iterações necessárias gauss: ", itGauss)
