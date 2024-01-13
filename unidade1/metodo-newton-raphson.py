def f(x):
  return x**2 - 21

# Vou definir a derivada, irei chamar de f_linha
def f_linha(x):
  return 2*x

# Irei fazer a função do Newton-Raphson
def metodo_newton():
  x0 = float(input("Digite uma aproximação inicial x0:")) # Terei que pedir uma aproximação inicial, que seria o ponto no eixo cartesiano. A variável x0 vai ser isso.
  iteracoes = 2
  i = 0

# Agora vou iniciar o cálculo do método. Vou começar com o laço while
  while i <= iteracoes:
    # Vou cálcular a raiz
    x1 = x0 - f(x0)/f_linha(x0)
    x0 = x1  # No final de cada iteração, irei atribuir a variável x0 com o valor de x1. Porque na próxima iteração, o valor que vai ser usado no lugar do x0 vai ser o x1. O x1 vai ser o x2 e, o x2 vai ser o x3 e assim sucessivamente.
    i+=1
  print("A raiz encontrada será: ", x1)

  # Se x1 é uma raiz de f(x), então f(x) tem que ser ZERO ou alguma coisa próxima a isso.
  print("f(x) =", f(x1))