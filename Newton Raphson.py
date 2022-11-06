import math as mt
import numpy as np
from sympy import *
e = 2.71828182846
x, y, z = symbols('x y z')
valor = 3

func = np.log(valor)


derivada_de_funcao = diff(ln(x) , x)
derivada_de_funcao = der
soma = valor - func / derivada_de_funcao
print(func,"\n",derivada_de_funcao)
print(soma)