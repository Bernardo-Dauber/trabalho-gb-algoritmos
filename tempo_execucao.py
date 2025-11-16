import time
from tabulate import tabulate
import matplotlib.pyplot as plt

# Matrizes de exemplo
m1 = [
    [1, -2],
    [3, 4]
]

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

# Move as definições das matrizes para antes do uso
m6 = [
    [2, -1, 3, 0, -2, 4],
    [-3, 5, -6, 2, 1, -4],
    [4, 2, -1, 3, -5, 2],
    [0, -2, 1, 4, 3, -1],
    [1, 3, -2, -3, 2, 5],
    [-4, 2, 3, -1, 0, 1]
]

m7 = [
    [1, -2, 3, 0, -2, 4, 2],
    [-3, 5, -6, 2, 1, -4, 3],
    [4, 2, -1, 3, -5, 2, -2],
    [0, -2, 1, 4, 3, -1, 1],
    [1, 3, -2, -3, 2, 5, -3],
    [-4, 2, 3, -1, 0, 1, 4],
    [2, -1, 0, 3, -2, 2, 1]
]

m8 = [
    [2, -1, 3, 0, -2, 4, 2, 1],
    [-3, 5, -6, 2, 1, -4, 3, 0],
    [4, 2, -1, 3, -5, 2, -2, 2],
    [0, -2, 1, 4, 3, -1, 1, -3],
    [1, 3, -2, -3, 2, 5, -3, 4],
    [-4, 2, 3, -1, 0, 1, 4, -2],
    [2, -1, 0, 3, -2, 2, 1, 3],
    [1, 2, -3, 4, 0, -1, 2, 5]
]

m9 = [
    [2, -1, 3, 0, -2, 4, 2, 1, -3],
    [-3, 5, -6, 2, 1, -4, 3, 0, 2],
    [4, 2, -1, 3, -5, 2, -2, 2, 1],
    [0, -2, 1, 4, 3, -1, 1, -3, 4],
    [1, 3, -2, -3, 2, 5, -3, 4, -2],
    [-4, 2, 3, -1, 0, 1, 4, -2, 3],
    [2, -1, 0, 3, -2, 2, 1, 3, -1],
    [1, 2, -3, 4, 0, -1, 2, 5, 2],
    [3, -2, 1, -4, 2, 0, 1, -3, 4]
]

m10 = [
    [2, -1, 3, 0, -2, 4, 2, 1, -3, 5],
    [-3, 5, -6, 2, 1, -4, 3, 0, 2, -1],
    [4, 2, -1, 3, -5, 2, -2, 2, 1, 3],
    [0, -2, 1, 4, 3, -1, 1, -3, 4, 2],
    [1, 3, -2, -3, 2, 5, -3, 4, -2, 1],
    [-4, 2, 3, -1, 0, 1, 4, -2, 3, -2],
    [2, -1, 0, 3, -2, 2, 1, 3, -1, 4],
    [1, 2, -3, 4, 0, -1, 2, 5, 2, -3],
    [3, -2, 1, -4, 2, 0, 1, -3, 4, 2],
    [0, 1, -2, 3, -1, 2, 4, -2, 1, 3]
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

matrizes = [
    ("2x2", m1),
    ("3x3", m2),
    ("4x4", m3),
    ("5x5", m4),
    ("6x6", m6),
    ("7x7", m7),
    ("8x8", m8),
    ("9x9", m9),
    ("10x10", m10)
]

resultados = []

for nome, matriz in matrizes:
    inicio = time.time()
    soma = melhor_soma_matriz(matriz)
    fim = time.time()
    tempo = fim - inicio
    resultados.append([nome, f"{len(matriz)}x{len(matriz[0])}", soma, f"{tempo:.6f} s"])


print(tabulate(resultados, headers=["Matriz", "Tamanho", "Melhor Soma", "Tempo Execução"]))

# Gerar diferentes tipos de gráficos com matplotlib
# Extrai nomes das matrizes e tempos de execução
nomes = [linha[0] for linha in resultados]
tempos = [float(linha[3].split()[0]) for linha in resultados]

# Salvar gráficos na pasta 'graficos'
# Gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(nomes, tempos, color='skyblue')
plt.xlabel('Matriz')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução por Matriz')
plt.tight_layout()
plt.savefig('graficos/tempo_execucao_barras.png')
plt.close()

# Gráfico de linhas
plt.figure(figsize=(8, 5))
plt.plot(nomes, tempos, marker='o', linestyle='-', color='green')
plt.xlabel('Matriz')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução por Matriz ')
plt.tight_layout()
plt.savefig('graficos/tempo_execucao_linhas.png')
plt.close()

# Gráfico de pizza
plt.figure(figsize=(7, 7))
plt.pie(tempos, labels=nomes, autopct='%1.4f s')
plt.title('Proporção do Tempo de Execução por Matriz ')
plt.tight_layout()
plt.savefig('graficos/tempo_execucao_pizza.png')
plt.close()

# Gráfico de barras horizontais (cada linha é uma matriz)
plt.figure(figsize=(8, 5))
plt.barh(nomes, tempos, color='orange')
plt.ylabel('Matriz')
plt.xlabel('Tempo de Execução (s)')
plt.title('Tempo de Execução por Matriz ')
plt.tight_layout()
plt.savefig('graficos/tempo_execucao_barras_horizontais.png')
plt.close()
