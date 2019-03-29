# -- coding: UTF-8 --
import numpy as np
import copy
def resolve_gauss(rigidez, forca, it, tol):
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

def resolve_jacobi(rigidez, forca, it, tol):
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
            return U,max(l_erro), i
    return U,max(l_erro),i






rigidez = 10**8*np.array([[1.59,-0.4, -0.54,1.2],[-0.4,1.7, 0.4,1.2], [-0.54, 0.4, 0.54,1.2],[-0.54, 1.4, 0.53,1.1] ])

forca = np.array([[0],[150], [-100],[30]])

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