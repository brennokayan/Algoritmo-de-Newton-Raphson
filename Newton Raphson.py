import math as mt
import numpy as np
import sympy as sp
e = 2.71828182846
x, y, z = sp.symbols('x y z')
valor = 3

func = np.log(valor)


derivada_de_funcao = sp.diff(sp.ln(x) , x)
a = derivada_de_funcao.split()
soma = valor - func / derivada_de_funcao
print(func,"\n",derivada_de_funcao)
print(soma)