# Importei a biblioteca de matemática 
import math

# Agora irei definir um intervalo [a, b] e também um erro
A = 4
B = 5
error = 0.0001

# Vou definir a função do cálculo
def f(x):
  return x**2 - 21

# Teorema de Bolzano
if f(A)*(B) < 0:
  while (math.fabs(B - A)/ 2 > error):
    xi = (A + B)/2
    if f(xi) == 0:
      print(" A raiz é:" , xi)
      break
    else: 
      if f(A)*f(xi) < 0:
        B = xi
      else:
        A = xi
  print("O valor da raiz é: ", xi)
else:
  print("Não há raiz neste intervalo!!")