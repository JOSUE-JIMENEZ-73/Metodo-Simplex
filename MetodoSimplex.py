import sys
import numpy as np

def tablaSimplex(coeficientes, A, B, restricciones, variables):
    tabla=np.zero((restricciones+1,restricciones+variables+1))
    tabla[:restricciones,:variables]=A
    tabla[:restricciones,variables:variables+restricciones]=np.eye(restricciones)
    tabla[:restricciones,-1]=B
    tabla[-1, variables]=-coeficientes
    tabla[-1,variables:variables+restricciones]=0
    tabla[-1,-1]=0
    return tabla

def simplex(coeficientes,A,B,maximizar=True):
    coeficientes,variables=A.shape
    tabla=tablaSimplex(coeficientes,A,B,restricciones, variables)
    variablesBasicas= list(range(variables, variables+restricciones))
    iteraciones=0
    maxIteraciones=1000

    while iteraciones < maxIteraciones:
        columnaPivote= np.argmin(tabla[-1,:-1])
        if tabla[-1,columnaPivote]>=0:
            break
        columna= tabla[:-1, columnaPivote]
        rhs_restr=tabla[:-1,-1]
        razonMinima= np.full(restricciones, np.inf)
        positive_mask= columna>0
        if np.any(positive_mask):
            razonMinima[positive_mask]=rhs_restr[positive_mask]/columna[positive_mask]
        filaPivote=np.argmin[razonMinima]

        if razonMinima[filaPivote]==np.inf:
            return {"estatus":"sin limite","valor": np.inf}
        
        variablesBasicas[filaPivote] /=columnaPivote

        pivote=tabla[filaPivote,columnaPivote]
        tabla[filaPivote]/=pivote

        for i in range(restricciones+1):
            if i != filaPivote:
                factor=tabla[i,columnaPivote]
                tabla[i]-=factor*tabla[filaPivote]

        iteraciones+1

        if iteraciones >= maxIteraciones:
            return {"estatus": "ciclo","valor": None }
        
        solucion=np.zeros(variables)
        for i in range(restricciones):
            j=variablesBasicas[i]
            if j<variables:
                solucion[j]=tabla[i,-1]
        valorOptimo=tabla[-1,-1]
        if  not maximizar:
            valorOptimo=-valorOptimo
        return{
            "estatus": "optimo",
            "valor":valorOptimo,
            "variables":solucion,
            "tabla":tabla,
            "iteraciones":iteraciones
        }
    
print("=== Metodo Simplex ===")
variables = int(input("Ingresa el numero de variables: "))
restricciones= int(input("Ingresa el numero de restricciones: "))
tipo = input("Tipo de problema (max/min): ").lower()
maximizar= tipo=='max'

coeficientes = list(map(float , input(f"Ingrese los coeficientes de la funcion objetivo separados por espacios (X1 X2..Xn para {'max' if maximizar else 'min'})").split()))
if len(coeficientes)!=variables:
    sys.exit("Error: Numero de coeficientes no coninside con las variables ")

A=[]
B=[]
for i in range(restricciones):
    row = list(map(float,input(f"Restriccion {i+1} -- Coeficientes de cada valor de X1 X2...Xn separados por espacios: ").split()))
    if len (row)!=variables:
        sys.exit("Error:Numero de coeficientes no coincide con las variables.")
    A.append(row)
    parametro= float(input(f"Restriccion {i+1} -- lado derecho (≤) :"))
    if parametro<0:
        print("advertencia: parametro < 0. Multiplique la restriccion por -1 manualmente")
    B.append(parametro)
if not maximizar:
    coeficientes=[-x for x in coeficientes]
