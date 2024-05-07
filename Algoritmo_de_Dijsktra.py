import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, id):
        self.id = id
        self.adyacentes = []
        self.recorrido = False
        self.padre = None
        self.distancia = float('inf')
    
    def agregar_adyacentes(self, v, p):
        if v not in self.adyacentes:
            self.adyacentes.append([v, p])

class Grafo:
    def __init__(self):
        self.G = nx.Graph()
        self.vertices = {}
    
    def dibujar_Grafo(self):
        pos = nx.layout.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()
    
    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)
    
    def agregar_aristas(self, vertice_inicial, vertice_final, peso):
        if vertice_inicial in self.vertices and vertice_final in self.vertices:
            self.vertices[vertice_inicial].agregar_adyacentes(vertice_final, peso)
            self.vertices[vertice_final].agregar_adyacentes(vertice_inicial, peso)
            self.G.add_edge(vertice_inicial, vertice_final, weight=peso)
    
    def camino_obtenido(self, vertice_final):
        camino = []
        actual = vertice_final
        while actual is not None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[vertice_final].distancia]
    
    def camino_corto(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]

            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v
    
    def Dijkstra(self, vertice_inicial):
        if vertice_inicial in self.vertices:
            self.vertices[vertice_inicial].distancia = 0
            actual = vertice_inicial
            sin_recorrer = []

            for v in self.vertices:
                if v != vertice_inicial:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                sin_recorrer.append(v)
            
            while len(sin_recorrer) > 0:
                for adyacente in self.vertices[actual].adyacentes:
                    if not self.vertices[adyacente[0]].recorrido:
                        if self.vertices[actual].distancia + adyacente[1] < self.vertices[adyacente[0]].distancia:
                            self.vertices[adyacente[0]].distancia = self.vertices[actual].distancia + adyacente[1]
                            self.vertices[adyacente[0]].padre = actual
                self.vertices[actual].recorrido = True
                sin_recorrer.remove(actual)

                actual = self.camino_corto(sin_recorrer)
        else:
            return False

if __name__ == '__main__':
    gf = Grafo()
    # Agregar los Vertices
    gf.agregar_vertice('a')
    gf.agregar_vertice('b')
    gf.agregar_vertice('c')
    gf.agregar_vertice('d')

    # Agregar las Aristas
    gf.agregar_aristas('a', 'b', 8)
    gf.agregar_aristas('a', 'c', 3)
    gf.agregar_aristas('b', 'd', 5)
    gf.agregar_aristas('c', 'b', 2)
    gf.agregar_aristas('c', 'd', 6)

    print("El camino más corto es:")
    gf.Dijkstra('a')
    print(gf.camino_obtenido('d'))

    gf.dibujar_Grafo()

