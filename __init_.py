import heapq

# Representa un nodo en el árbol de búsqueda
class Nodo:
    def __init__(self, ciudad, padre=None, costo_camino=0, heuristica=0):
        self.ciudad = ciudad
        self.padre = padre
        self.costo_camino = costo_camino
        self.heuristica = heuristica

    def __lt__(self, otro):
        return (self.costo_camino + self.heuristica) < (otro.costo_camino + otro.heuristica)


# Algoritmo A*
def a_estrella(inicio, objetivo, conexiones, heuristica):
    nodo_inicio = Nodo(inicio, None, 0, heuristica[inicio])
    nodo_objetivo = Nodo(objetivo)

    nodos_abiertos = [nodo_inicio]
    nodos_cerrados = set()

    while nodos_abiertos:
        # Añade al final de la lista y ordena
        actual = heapq.heappop(nodos_abiertos)

        if actual.ciudad == objetivo:
            camino = []
            while actual:
                camino.insert(0, actual.ciudad)
                actual = actual.padre
            return camino

        nodos_cerrados.add(actual.ciudad)

        for vecino, costo in conexiones[actual.ciudad].items():
            if vecino in nodos_cerrados:
                continue

            nuevo_costo_camino = actual.costo_camino + costo
            nuevo_nodo = Nodo(vecino, actual, nuevo_costo_camino, heuristica[vecino])

            if any(nodo.ciudad == vecino and nodo.costo_camino <= nuevo_costo_camino for nodo in nodos_abiertos):
                continue

            heapq.heappush(nodos_abiertos, nuevo_nodo)

    return None

# Diccionario de conexiones entre ciudades y sus distancias
conexiones = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucarest': 101, 'Craiova': 138},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'Drobeta': {'Craiova': 120, 'Mehadia': 75},
    'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Bucarest': {'Fagaras': 211, 'Pitesti': 101}
}

# Diccionario de heurística (distancia estimada a Bucarest desde cada ciudad)
heuristica = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 178,
    'Rimnicu Vilcea': 193,
    'Pitesti': 98,
    'Craiova': 160,
    'Drobeta': 242,
    'Mehadia': 241,
    'Lugoj': 244,
    'Timisoara': 329,
    'Bucarest': 0
}

inicio = ''
while True:
    inicio = input("Ingrese la ciudad de inicio: ")
    if inicio in conexiones:
        break
    else:
        print("Ciudad inválida.")
        

objetivo = 'Bucarest'

camino = a_estrella(inicio, objetivo, conexiones, heuristica)

if camino:
    print(f"Camino encontrado: {camino}")
else:
    print("No se encontró un camino.")
