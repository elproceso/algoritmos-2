def ordenamiento_burbuja(lista):
    n = len(lista)
    # Recorre toda la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Compara los elementos adyacentes
            if lista[j] > lista[j+1]:
                # Intercambia si el elemento encontrado es mayor
                # que el siguiente elemento
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = ordenamiento_burbuja(lista)
print("Lista ordenada:", lista_ordenada)
