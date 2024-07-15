from collections import deque

def bfs_cajas_y_conejos(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Encontrar la posición inicial del BFS (la posición del conejo)
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'C':
                start = (r, c)
                break
        if start:
            break
    
    if not start:
        return "No hay conejo en la cuadrícula"
    
    # Direcciones para moverse en la cuadrícula (arriba, abajo, izquierda, derecha)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Cola para el BFS
    queue = deque([start])
    
    # Conjunto para almacenar las celdas visitadas
    visited = set([start])
    
    while queue:
        current = queue.popleft()
        r, c = current
        
        # Procesar la celda actual (aquí solo imprimimos su posición)
        print(f"Visitando celda: {current}")
        
        # Explorar las celdas adyacentes
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Comprobar que la nueva posición está dentro de los límites y no ha sido visitada
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] == '0':  # Solo se puede mover a cajas vacías
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                elif grid[nr][nc] == 'C':  # Si encuentra otro conejo
                    print(f"Conejo encontrado en: ({nr}, {nc})")
                    return (nr, nc)
    
    return "No se encontró otro conejo"

# Ejemplo de uso
grid = [
    ['0', '1', '0', '0', '0'],
    ['0', '1', 'C', '1', '0'],
    ['0', '0', '0', '0', '0'],
    ['1', '1', '0', '1', '1'],
    ['0', 'C', '0', '0', '0']
]

print(bfs_cajas_y_conejos(grid))
