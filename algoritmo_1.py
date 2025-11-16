'''
0 0 1 0
9 2 -6 2
-3 2 -4 1
-2 6 0 -3
'''

# Matriz 4x4 (já usada no seu código)
m3 = [
    [0, 0, 1, 0],
    [9, 2, -6, 2],
    [-3, 2, -4, 1],
    [-2, 6, 0, -3]
]

m = m3
def kadane(arr):
    max_atual = max_total = arr[0]
    for x in arr[1:]:
        max_atual = max(x, max_atual + x)
        max_total = max(max_total, max_atual)
    return max_total

N = len(m)
melhor_soma = float('-inf')

for i in range(N):
    for j in range(i, N):
        temp = [0] * N
        for k in range(i, j + 1):
            for c in range(N):
                temp[c] += m[k][c]
        soma_atual = kadane(temp)
        if soma_atual > melhor_soma:
            melhor_soma = soma_atual

print("Melhor soma:", melhor_soma)



