import random
import pandas as pd
import numpy as np
from scipy.stats import binom


def encontrar_alef(maze):
    """
    Encontra a posição inicial de Alef (marcado com 'A') no labirinto.
    Retorna uma tupla (i, j) com as coordenadas.
    """
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'A':
                return (i, j)
    return None

def criar_mapa_tuneis(tunnels):
    """
    Cria um dicionário que mapeia as entradas e saídas dos túneis.
    Cada entrada é ligada à sua saída, e vice-versa.
    """
    mapa = {}
    for i1, j1, i2, j2 in tunnels:
        mapa[(i1, j1)] = (i2, j2)
        mapa[(i2, j2)] = (i1, j1)
    return mapa

def resolver_labirinto(n, m, k, maze, tunnels):

    start = encontrar_alef(maze)         # Encontra onde está o 'A'
    mapa_tuneis = criar_mapa_tuneis(tunnels)  # Constrói o mapa dos túneis
    visitado = set()                     # Guarda as células visitadas (para evitar ciclos infinitos)

    def dfs(pos):
        """
        Função recursiva que simula todos os caminhos possíveis e
        retorna a probabilidade de sucesso a partir da posição 'pos'.
        """
        if pos in visitado:
            return 0.0  # Já visitado = evita loops
        visitado.add(pos)

        i, j = pos
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
        opcoes = []

        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                celula = maze[ni][nj]
                if celula != '#':  # Se não for obstáculo
                    opcoes.append((ni, nj))

        if not opcoes:
            return 0.0  # Alef está preso, sem para onde ir

        soma_prob = 0.0
        for ni, nj in opcoes:
            celula = maze[ni][nj]

            if celula == '*':
                prob = 0.0  # Morreu
            elif celula == '%':
                prob = 1.0  # Escapou
            elif (ni, nj) in mapa_tuneis:
                destino = mapa_tuneis[(ni, nj)]  # Vai para outra entrada do túnel
                prob = dfs(destino)
            else:
                prob = dfs((ni, nj))  # Caminho normal

            soma_prob += prob

        return soma_prob / len(opcoes)  # Média da probabilidade

    return dfs(start)

def gerar_labirinto(n, m):
 elementos = ['O']*5 + ['#', '*', '%']
 labirinto = [''.join(random.choice(elementos) for _ in range(m)) for _ in range(n)]
 i, j = random.randint(0, n-1), random.randint(0, m-1)
 linha = list(labirinto[i])
 linha[j] = 'A'
 labirinto[i] = ''.join(linha)
 return labirinto


def gerar_tuneis(k, n, m):
 tuneis = set()  #cria objetos
 while len(tuneis) < k:
   i1, j1 = random.randint(0, n-1), random.randint(0, m-1)
   i2, j2 = random.randint(0, n-1), random.randint(0, m-1)
   if (i1 != i2 or j1 != j2):
     tuneis.add((i1, j1, i2, j2))
     return list(tuneis)


def main():
 n, m, k = 5, 6, 2
 maze = gerar_labirinto(n, m)
 tunnels = gerar_tuneis(k, n, m)
 print("Maze:")
 for linha in maze:
   print(linha)
   print("Tunnels:", tunnels)
   resultado = resolver_labirinto(n, m, k, maze, tunnels)
   print("Probabilidade de fuga:", resultado)
if __name__ == '__main__':
   main()