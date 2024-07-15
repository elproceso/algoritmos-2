def dfs(grafo, nodo_inicio, nodo_destino, camino=None, visitado=None):
    if camino is None:
        camino = []
    if visitado is None:
        visitado = set()

    # Marca el nodo actual como visitado
    visitado.add(nodo_inicio)
    camino.append(nodo_inicio)

    # Si llegamos al nodo destino, devolvemos el camino
    if nodo_inicio == nodo_destino:
        return camino

    # Recorremos los nodos vecinos
    for vecino in grafo.get(nodo_inicio, []):
        if vecino not in visitado:
            resultado = dfs(grafo, vecino, nodo_destino, camino[:], visitado)
            if resultado is not None:
                return resultado

    # Si no se encontró el nodo destino, se elimina el nodo actual del camino
    return None

# Ejemplo de uso:
# El grafo está representado como un diccionario donde las claves son nodos y los valores son listas de nodos vecinos
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

nodo_inicio = 'A'
nodo_destino = 'G'

ruta = dfs(grafo, nodo_inicio, nodo_destino)
if ruta:
    print("Ruta encontrada:", ruta)
else:
    print("No se encontró una ruta.")

