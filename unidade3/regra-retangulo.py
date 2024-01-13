import numpy as np  

def f(x):
    return 4*(x**3)

# Regra retângulo
def regraRetangulo(a, b, n):
    
    h = (b-a)/n       # Tamanho de cada subintervalo
    integral = 0
    for i in range(n):
        x = a + i*h     # Ponto inicial do retângulo
        integral += f(x)  # Área do retângulo
    integral *= h
    
    return integral

a = 0
b = 4
n = 100

resultado = regraRetangulo(a, b, n)

print("Regra retângulo: ")
print(resultado)


# Ponto Médio
def pontoMedio(a, b, n):
    
    h = (b-a)/n  # Tamanho de cada subintervalo
    integral = 0
    for i in range(n):
        x = a + (i+0.5)*h # Ponto médio do subintervalo
        integral += f(x) # Área do retângulo
    integral *= h
    
    return integral

a = 0
b = 4
n = 100

resultado = pontoMedio(a, b, n)

print("\nRegra do ponto médio: ")
print(resultado)


# Regra Trapézio
def regraTrapezio(a, b, n):
    
    h = (b-a)/n    # Tamanho de cada subintervalo
    integral = 0
    for i in range(n):
        x0 = a + i * h  # Extremidade esquerda do subintervalo
        x1 = x0 + h  # Extremidade direita do subintervalo
        integral += (f(x0) + f(x1))/2  # Área do trapézio
    integral *= h
  
    return integral

a = 0
b = 4
n = 100

resultado = regraTrapezio(a, b, n)

print("\nRegra do trapézio: ")
print(resultado)


# Regra Simpson
def regraSimpson(a, b, n):
    
    h = (b - a) / n  # Tamanho de cada subintervalo
    integral = 0
    for i in range(n):
        x0 = a + i * h  # Extremidade esquerda do subintervalo
        x1 = a + (i + 0.5) * h  # Ponto médio do subintervalo
        x2 = a + (i + 1) * h  # Extremidade direita do subintervalo
        integral += (f(x0) + 4*f(x1) + f(x2)) * h / 6  # Área sob o segmento parabólico
    return integral

a = 0
b = 4
n = 100

resultado = regraSimpson(a, b, n)

print("\nRegra do Simpsom: ")
print(resultado)