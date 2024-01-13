def f(x):
  return x**2 - 21

def metodo_secante():
  x0 = float(input("Digite uma aproximação inicial x0:"))
  x1 = float(input("Digite uma aproximação inicial x1:"))
  iteracoes = int(input("Digite o número de iterações: "))
  i = 0

# Agora vou iniciar o cálculo do método. 
  while i <= iteracoes:
      x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
      x0 = x1
      x1 = x2
      i =+1
  print("A raiz encontrada foi x= ", x2)
  print("f(x)= ", f(x2)) # O f(x) tem que ser próximo de zero ou ser o próprio zero.