def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, fila):
    print("Matriz original:")
    for row in matriz:
        print(row)
    bubble_sort(matriz[fila])
    print(f"\nMatriz con la fila {fila} ordenada:")
    for row in matriz:
        print(row)

matriz = [
    [5, 8, 12],
    [9, 3, 7],
    [4, 6, 10]
]

fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)
