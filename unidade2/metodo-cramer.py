def metodoCramer(a11, a12, b1, a21, a22, b2):
    D = a11 * a22 - a12 * a21
    D1 = b1 * a22 - b2 * a12
    D2 = a11 * b2 - a21 * b1
  
    #Verificando se o sistema é possível
    if D != 0:
        # Cálculo das soluções
        x1 = D1 / D
        x2 = D2 / D
        return x1, x2
    else:
        return None
    
a11 = 2    #Exemplo de sistema linear
a12 = 3
b1 = 8
a21 = 4
a22 = -2
b2 = -2

solucao = metodoCramer(a11, a12, b1, a21, a22, b2)

#Verificação da existência de solução
if solucao is not None:
    x1, x2 = solucao
    print("A solução é:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("Sistema indeterminado.")