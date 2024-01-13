def jacobi(A,b,vetorSolucao,iteracoes):
  iteracao = 0
  vetorAuxiliar = []
  for k in range(len(vetorSolucao)):
    vetorAuxiliar.append(0)

  while iteracao < iteracoes:
    for i in range(len(A)):
      x = b[i]
      for j in range(len(A)):
        if i != j:
          x-= A[i][j]*vetorSolucao[j]
      x /= A[i][i]
      vetorAuxiliar[i] = x
    iteracao += 1

    for p in range(len(vetorAuxiliar)):
      vetorSolucao[p] = vetorAuxiliar[p]

  print(vetorSolucao)

def metodoGaussseidel(A, b, vetorSolucao, iteracoes):
  iteracao = 0
  while iteracao < iteracoes:
    for i in range(len(A)):
      x = b[i]
      for j in range(len(A)):
        if i !=j:
          x-= A[i][j]*vetorSolucao[j]
      x/= A[i][i]
      vetorSolucao[i] = x
    iteracao += 1


  print(vetorSolucao)


A = [[5,1,1],[3,4,1],[3,3,6]]
b = [5,6,0]
vetorSolucao = [0,0,0]
iteracoes = 200

jacobi(A,b,vetorSolucao,iteracoes)
metodoGaussseidel(A, b, vetorSolucao, iteracoes)