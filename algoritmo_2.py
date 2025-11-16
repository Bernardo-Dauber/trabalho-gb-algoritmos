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