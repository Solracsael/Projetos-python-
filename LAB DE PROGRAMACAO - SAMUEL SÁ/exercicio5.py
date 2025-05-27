from collections import defaultdict
import random

def similar_pair(n, k, edges):
    tree = defaultdict(list)
    filhos = set()

    # Monta a árvore e identifica os filhos
    for pai, filho in edges:
        tree[pai].append(filho)
        filhos.add(filho)

    # A raiz é o nó que nunca aparece como filho
    raiz = next(i for i in range(1, n + 1) if i not in filhos)

    count = 0

    # DFS com lista de ancestrais
    def dfs(atual, ancestrais):
        nonlocal count
        for anc in ancestrais:
            if abs(anc - atual) <= k:
                count += 1
        for filho in tree[atual]:
            dfs(filho, ancestrais + [atual])

    dfs(raiz, [])
    return count

def generateTestCases():
    return [
        (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)]),
        (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]),
        (4, 1, [(1, 2), (2, 3), (3, 4)]),
        (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]),
        (3, 0, [(1, 2), (2, 3)])
    ]

def main():
    testCases = generateTestCases()
    for idx, (n, k, edges) in enumerate(testCases, 1):
        print(f"🧪 Teste {idx}")
        print(f"n = {n}, k = {k}, edges = {edges}")
        result = similar_pair(n, k, edges)
        print(f"➡️ Resultado: {result}\n")

if __name__ == "__main__":
    main()
