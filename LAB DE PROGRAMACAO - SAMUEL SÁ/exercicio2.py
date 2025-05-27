import random

def insertionSort(arr):
    deslocamentos = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover elementos maiores que key para frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            deslocamentos += 1  # cada vez que movemos um número, é um deslocamento
        arr[j + 1] = key
    return deslocamentos

def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    t = int(input())  # número de casos de teste
    for _ in range(t):
        n = int(input())  # tamanho do vetor
        arr = list(map(int, input().split()))  # vetor
        result = insertionSort(arr)
        print(result)

if __name__ == '__main__':
    main()
