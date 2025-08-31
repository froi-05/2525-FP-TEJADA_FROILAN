def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

matriz = [
    [5, 8, 12],
    [9, 3, 7],
    [4, 6, 10]
]

valor_a_buscar = 7
posicion = buscar_valor(matriz, valor_a_buscar)

if posicion:
    print(f"Valor {valor_a_buscar} encontrado en la posición: {posicion}")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz")
