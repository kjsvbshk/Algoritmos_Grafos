from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.visited = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.visited[u].append(False)
        self.visited[v].append(False)

    def removeEdge(self, u, v):
        if v in self.graph[u]:
         self.graph[u].remove(v)
        if u in self.graph[v]:
         self.graph[v].remove(u)
        if v in self.visited[u]:
         self.visited[u].remove(v)
        if u in self.visited[v]:
         self.visited[v].remove(u)


    def DFS(self, v):
        stack = []
        stack.append(v)

        while stack:
            curr_vertex = stack[-1]
            stack.pop()

            if not self.visited[v]:
                self.visited[v] = True

            for index, adj_vertex in enumerate(self.graph[curr_vertex]):
                if not self.visited[curr_vertex][index]:
                    break

            if not self.visited[curr_vertex][index]:
                stack.append(curr_vertex)
                self.visited[curr_vertex][index] = True
                stack.append(adj_vertex)

    def hasEulerianPath(self):
        odd_degrees = 0
        for v in self.graph:
            if len(self.graph[v]) % 2 != 0:
                odd_degrees += 1

        if odd_degrees == 0 or odd_degrees == 2:
            return True
        return False

    def findEulerianPath(self):
        if not self.hasEulerianPath():
            return None

        start_vertex = 0
        for v in self.graph:
            if len(self.graph[v]) % 2 != 0:
                start_vertex = v
                break

        self.DFS(start_vertex)

        path = []
        for v in self.graph:
            for index, adj_vertex in enumerate(self.graph[v]):
                if self.visited[v][index]:
                    path.append(v)
                    path.append(adj_vertex)
                    self.removeEdge(v, adj_vertex)
                    break

        return path

    def printGraph(self):
        for v in self.graph:
            print(f"Vértice {v}: ", end="")
            for u in self.graph[v]:
                print(u, end=" ")
            print()


# Función para dibujar el grafo utilizando NetworkX
def draw_graph(graph):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for v in graph.graph:
        for u in graph.graph[v]:
            G.add_edge(v, u)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
    plt.show()


# Función para crear un grafo a partir de una matriz de adyacencia
def create_graph_from_adjacency_matrix(adj_matrix):
    graph = Graph(len(adj_matrix))
    for v in range(len(adj_matrix)):
        for u in range(len(adj_matrix[v])):
            if adj_matrix[v][u] == 1:
                graph.addEdge(v, u)
    return graph


# Función para mostrar el camino de Euler
def print_eulerian_path(path):
    if path is None:
        print("No existe camino de Euler en el grafo dado")
    else:
        print("Camino de Euler:", end=" ")
        for vertex in path:
            print(vertex, end=" ")
        print()


# Ingresar el grafo como una matriz de adyacencia
adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 0]
]

# Crear el grafo a partir de la matriz de adyacencia
graph = create_graph_from_adjacency_matrix(adjacency_matrix)

# Mostrar el grafo ingresado
print("Grafo ingresado:")
graph.printGraph()
draw_graph(graph)

# Encontrar el camino de Euler
path = graph.findEulerianPath()

# Mostrar el camino de Euler encontrado
print_eulerian_path(path)
