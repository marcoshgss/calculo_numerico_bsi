def gaussJordan(A, b):

  # O n é a ordem da matriz A.
  n= len(A)
  # vai até a última coluna.
  for k in range(0, n): 
    
    # Transforma o pivô em 1
    for j in range(k+1, n):
      A[k][j] = A[k][j]/A[k][k]
    b[k] = b[k] /A[k][k]
    A[k][k] = 1
    
    # para cada linha i
    for i in range(0, n):
      if i != k:
        # Calcula o fator m
        m = - A[i][k]/A[k][k]
  
        for j in range(k+1, n):
          A[i][j] = m * A[k][j] + A[i][j]
        # Vai atualizar o vetor b na linha i.
        b[i] = m * b[k] + b[i]
  
        A[i][k] = 0
  return b