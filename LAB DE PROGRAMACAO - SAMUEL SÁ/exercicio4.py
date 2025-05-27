import re
from itertools import product
import random

MOD = 10**9 + 7

def countRecognizedStrings_brute(R, L):
    pattern = re.compile(f"^{R}$")
    count = 0
    for p in product("ab", repeat=L):
        s = ''.join(p)
        if pattern.fullmatch(s):
            count += 1
    return count % MOD

def gerar_expressao():
    # Simples gerador de expressões balanceadas
    bases = ["a", "b"]
    exp = random.choice(bases)
    for _ in range(random.randint(1, 3)):
        op = random.choice(["|", "", "*"])
        if op == "":
            exp = f"({exp}{random.choice(bases)})"
        elif op == "|":
            exp = f"({exp}|{random.choice(bases)})"
        elif op == "*":
            exp = f"({exp}*)"
    return exp

def main():
    T = 3
    casos = []
    for _ in range(T):
        R = gerar_expressao()
        L = random.randint(1, 6)
        casos.append((R, L))
    for R, L in casos:
        print(f"Expressão: {R}, Tamanho: {L}")
        resultado = countRecognizedStrings_brute(R, L)
        print("Reconhecidas:", resultado)

if __name__ == '__main__':
    main()
