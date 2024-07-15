import heapq

# Clase para representar el grafo
class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_arista(self, desde, hasta, peso):
        if desde not in self.nodos:
            self.nodos[desde] = []
        if hasta not in self.nodos:
            self.nodos[hasta] = []
        self.nodos[desde].append((hasta, peso))
        self.nodos[hasta].append((desde, peso))

# Función para encontrar el conejo más cercano usando el algoritmo de Dijkstra
def encontrar_conejo_mas_cercano(grafo, inicio, conejos):
    distancia = {nodo: float('infinity') for nodo in grafo.nodos}
    distancia[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual in conejos:
            return nodo_actual, distancia_actual

        for vecino, peso in grafo.nodos[nodo_actual]:
            distancia_a_traves_de_actual = distancia_actual + peso
            if distancia_a_traves_de_actual < distancia[vecino]:
                distancia[vecino] = distancia_a_traves_de_actual
                heapq.heappush(cola_prioridad, (distancia_a_traves_de_actual, vecino))
    
    return None, float('infinity')

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('A', 'C', 4)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('B', 'D', 5)

# Supongamos que los conejos están en las cajas 'C' y 'D'
conejos = {'C', 'D'}

# Encontrar el conejo más cercano desde la caja 'A'
inicio = 'A'
nodo_conejo, distancia_conejo = encontrar_conejo_mas_cercano(grafo, inicio, conejos)

print(f"El conejo más cercano está en la caja {nodo_conejo} a una distancia de {distancia_conejo}")
