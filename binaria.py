def busqueda_binaria_cajas(cajas, conejo):
    izquierda = 0
    derecha = len(cajas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if cajas[medio] == conejo:
            return medio  # Se encontró el conejo en la caja con índice medio
        elif cajas[medio] < conejo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda

    return -1  # El conejo no se encuentra en ninguna caja

# Lista de cajas (ordenada)
cajas = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Conejo que queremos encontrar
conejo = 13

# Llamada a la función de búsqueda binaria
resultado = busqueda_binaria_cajas(cajas, conejo)

if resultado != -1:
    print(f"El conejo está en la caja con índice {resultado}.")
else:
    print("El conejo no se encuentra en ninguna caja.")
