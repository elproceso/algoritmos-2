def buscar_conejo(cajas):
    """
    Busca un conejo en una lista de cajas.

    :param cajas: Lista de cajas donde cada caja puede o no contener un conejo.
    :return: El índice de la caja que contiene el conejo, o -1 si no se encuentra ningún conejo.
    """
    for i, caja in enumerate(cajas):
        if caja == "conejo":
            return i
    return -1

# Ejemplo de uso
cajas = ["libro", "juguete", "conejo", "pelota"]
indice_conejo = buscar_conejo(cajas)

if indice_conejo != -1:
    print(f"El conejo está en la caja número {indice_conejo}.")
else:
    print("No se encontró ningún conejo.")
