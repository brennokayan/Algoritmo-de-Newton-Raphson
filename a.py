import math as mt
import numpy as np
import sympy as sp
soma = 0
func = "ln 2 + 3"
func1, var_func1, sinal, func2 = func.split()
# result = np.log(var_func1)
var_func1 = int(var_func1)
result = type(var_func1)
if (func1 == 'ln'):
    resultado = np.log(var_func1)
    print(resultado)
if(sinal == '+'):
    soma = resultado + func2
print(resultado)