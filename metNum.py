# -- coding: UTF-8 --
import numpy as np
import copy
def resolve_gauss(rigidez, forca, it, tol,BCNodes):
    n=len(rigidez)
    U = np.zeros((n,1))
    i = 0
    while (i<it):
        l_erro = []
        for j in range(n):
            U_anterior = copy.copy(U)
            U[j] = forca[j]



            for k in range(n-j):
                if k!=j:
                    U[j]-=(rigidez[j,k]*U_anterior[k])
            for l in range(j):
                if l!=j:
                    U[j]-=rigidez[j,l]*U[l]



            U[j]=U[j]/rigidez[j,j]
            if(U[j] == j):
                erro = 0
            else:
                erro = ((U[j] - U_anterior[j])/U[j])
            l_erro.append(erro)
        i+=1
        if erro<tol:
            return U,max(l_erro), i+1
    return U,max(l_erro),i

def resolve_jacobi(rigidez, forca, it, tol,BCNodes):
    n=len(rigidez)
    U = np.zeros((n,1))
    i = 0
    while (i<it):
        l_erro = []
        U_anterior =  copy.copy(U)
        for j in range(n):
            U[j] = forca[j]
            for k in  range(n):
                if k!=j:
                    U[j]-=(rigidez[j,k]*U_anterior[k])
            U[j]=U[j]/rigidez[j,j]
            if(U[j] == j):
                erro = 0
            else:
                erro = ((U[j] - U_anterior[j])/U[j])
            l_erro.append(erro)
        i+=1
        if erro<tol:
            itera=i
            break
    Listaresp=[]
    l=0
    for k in range(2*n):
        if (k+1) in BCNodes:
            Listaresp.append(U[l])
            l+=1 
        else:
            Listaresp.append(0)
    DicResp ={}
    No=0
    for D in range(n):
        DicResp[D+1]=[float(Listaresp[No]),float(Listaresp[No+1])]
        No+=2
    return DicResp,max(l_erro),itera






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
# U_gauss, erro_gauss,itGauss = resolve_gauss(rigidez, forca, it, tol,BCNodes)
# print("U gauss: ", U_gauss)
# print("Erro gauss: ",erro_gauss)
# print("Iterações necessárias gauss: ", itGauss)
