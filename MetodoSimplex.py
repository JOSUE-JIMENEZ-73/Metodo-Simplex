import sys
import numpy as np

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
    parametro= float(input(f"Restriccion {i+1} -- lado derecho (<=) :"))
    if parametro<0:
        print("advertencia: parametro < 0. Multiplique la restriccion por -1 manualmente")
    B.append(parametro)
if not maximizar:
    coeficientes=[-x for x in coeficientes]
np.array(coeficientes),np.array(A), np.array(B),maximizar