import time
from tabulate import tabulate
import matplotlib.pyplot as plt

# Matrizes de exemplo
m2 = [
    [0, -2, 3],
    [4, 5, -6],
    [-7, 8, 9]
]

m3 = [
    [0, 0, 1, 0],
    [9, 2, -6, 2],
    [-3, 2, -4, 1],
    [-2, 6, 0, -3]
]

m4 = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6],
    [0, -4, 10, -5, 1]
]


def kadane(arr):
    max_atual = max_total = arr[0]
    for x in arr[1:]:
        max_atual = max(x, max_atual + x)
        max_total = max(max_total, max_atual)
    return max_total


def melhor_soma_matriz(m):
    N = len(m)
    melhor_soma = float('-inf')
    for i in range(N):
        for j in range(i, N):
            temp = [0] * len(m[0])
            for k in range(i, j + 1):
                for c in range(len(m[0])):
                    temp[c] += m[k][c]
            soma_atual = kadane(temp)
            if soma_atual > melhor_soma:
                melhor_soma = soma_atual
    return melhor_soma


def forca_bruta(matriz):
    tamanho = len(matriz)
    soma_maxima = float('-inf')
    melhor_configuracao = None

    for linha_superior in range(tamanho):
        for linha_inferior in range(linha_superior, tamanho):
            for coluna_esquerda in range(tamanho):
                for coluna_direita in range(coluna_esquerda, tamanho):
                    soma_atual = 0
                    for linha in range(linha_superior, linha_inferior + 1):
                        for coluna in range(coluna_esquerda, coluna_direita + 1):
                            soma_atual += matriz[linha][coluna]
                    if soma_atual > soma_maxima:
                        soma_maxima = soma_atual
                        melhor_configuracao = (linha_superior, linha_inferior, coluna_esquerda, coluna_direita)
    print("Soma máxima encontrada: {}".format(soma_maxima))
    return soma_maxima


matrizes = [
    ("3x3", m2),
    ("4x4", m3),
    ("5x5", m4)
]

resultados = []

for nome, matriz in matrizes:
    inicio = time.time()
    soma_melhor = melhor_soma_matriz(matriz)
    fim = time.time()
    tempo_melhor = fim - inicio

    inicio = time.time()
    soma_bruta = forca_bruta(matriz)
    fim = time.time()
    tempo_bruta = fim - inicio

    resultados.append([nome, soma_melhor, tempo_melhor, soma_bruta, tempo_bruta])

print(tabulate(resultados, headers=["Matriz", "Melhor Soma (Kadane)", "Tempo Kadane", "Melhor Soma (Força Bruta)", "Tempo Força Bruta"]))

# Gerar gráficos comparativos
nomes = [linha[0] for linha in resultados]
tempos_kadane = [linha[2] for linha in resultados]
tempos_bruta = [linha[4] for linha in resultados]

# Gráfico de barras comparativo
plt.figure(figsize=(8, 5))
bar_width = 0.35
indices = range(len(nomes))
plt.bar(indices, tempos_kadane, bar_width, label='Kadane', color='blue')
plt.bar([i + bar_width for i in indices], tempos_bruta, bar_width, label='Força Bruta', color='red')
plt.xlabel('Matriz')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempo de Execução')
plt.xticks([i + bar_width / 2 for i in indices], nomes)
plt.legend()
plt.tight_layout()
plt.savefig('graficos/comparacao_tempo_barras.png')
plt.close()

# Gráfico de linhas comparativo
plt.figure(figsize=(8, 5))
plt.plot(nomes, tempos_kadane, marker='o', linestyle='-', color='blue', label='Kadane')
plt.plot(nomes, tempos_bruta, marker='o', linestyle='-', color='red', label='Força Bruta')
plt.xlabel('Matriz')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempo de Execução')
plt.legend()
plt.tight_layout()
plt.savefig('graficos/comparacao_tempo_linhas.png')
plt.close()
