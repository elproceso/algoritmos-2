import heapq

def heuristica(a, b):
    """Calcula la heurística de la distancia de Manhattan entre dos puntos."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    """Implementación del algoritmo A*."""
    filas, columnas = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristica(start, goal)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < filas and 0 <= neighbor[1] < columnas:
                if maze[neighbor[0]][neighbor[1]] == 1:
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristica(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

# Ejemplo de uso:
laberinto = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 'R']
]
inicio = (0, 0)
meta = (4, 4)

camino = astar(laberinto, inicio, meta)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")
