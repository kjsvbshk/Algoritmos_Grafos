import networkx as nx
import matplotlib.pyplot as plt

def graph_coloring(graph):
    colors = {}  # Diccionario para almacenar el color asignado a cada nodo

    # Recorrer los nodos en orden y asignar un color válido
    for node in graph.nodes():
        # Obtener los colores asignados a los nodos vecinos
        neighbor_colors = set(colors.get(neighbor, None) for neighbor in graph.neighbors(node))

        # Encontrar el primer color disponible
        for color in range(len(graph.nodes())):
            if color not in neighbor_colors:
                colors[node] = color
                break

    return colors

# Matriz de adyacencia del grafo (ejemplo)
adjacency_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
]

# Crear lista de aristas a partir de la matriz de adyacencia
edges = []
for i in range(len(adjacency_matrix)):
    for j in range(i+1, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            edges.append((i, j))

# Crear grafo a partir de la lista de aristas
graph = nx.from_edgelist(edges)

# Obtener los colores asignados a cada nodo
colors = graph_coloring(graph)

# Imprimir los colores asignados a cada nodo
print("Colores asignados a cada Vertice:")
for node, color in colors.items():
    if color == 0:
        color_name = 'Rojo'
    elif color == 1:
        color_name = 'Naranja'
    elif color == 2:
        color_name = 'Gris'
    elif color == 3:
        color_name = 'Verde'
    else:
        color_name = f'Color {color}'
    print(f"Vertice {node}: Color {color_name}")

# Visualizar el grafo con los colores asignados
node_colors = [colors.get(node, None) for node in graph.nodes()]
nx.draw(graph, with_labels=True, node_color=node_colors, cmap=plt.cm.Set1)

plt.show()
