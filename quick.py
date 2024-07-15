def quicksort(arr):
    """
    Función principal de QuickSort que ordena una lista.
    :param arr: Lista de elementos a ordenar.
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr
    else:
        # Elegir un pivote (en este caso, el último elemento de la lista)
        pivote = arr[-1]
        # Listas para elementos menores, iguales y mayores que el pivote
        menores = [x for x in arr[:-1] if x <= pivote]
        mayores = [x for x in arr[:-1] if x > pivote]
        # Llamada recursiva para ordenar las sublistas y combinar con el pivote
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
lista = [3, 6, 8, 10, 1, 2, 1]
print("Lista original:", lista)
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)
