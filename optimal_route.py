from dataset import knowledge_base


# Implementación del algoritmo de búsqueda A*
def determine_optimal_route(origen, destination, knowledge_base):
    """
    Encuentra la mejor ruta desde el origen hasta el destino utilizando el algoritmo A*.
    """
    # Inicializamos la lista de nodos abiertos y cerrados
    open_nodes = [(origen, 0, [])]
    closed_nodes = []

    # Bucle principal del algoritmo A*
    while open_nodes:
        # Seleccionamos el nodo actual con el menor coste estimado hasta el destino
        current_node = min(open_nodes, key=lambda x: x[1] + calculate_heuristic(x[0], destination))
        current_station, current_cost, current_route = current_node

        # Comprobamos si hemos llegado al destino
        if current_station == destination:
            return current_route + [current_station]

        # Movemos el nodo actual de la lista de abiertos a la de cerrados
        open_nodes.remove(current_node)
        closed_nodes.append(current_node)

        # Expandimos el nodo actual y exploramos sus conexiones
        for station, cost in knowledge_base["conexiones"].get(current_station, []):
            total_cost = current_cost + cost
            next_node = (station, total_cost, current_route + [station])

            # Verificamos si el nodo ya ha sido explorado o si es una mejor opción
            if next_node not in closed_nodes:
                if next_node not in open_nodes:
                    open_nodes.append(next_node)
                else:
                    index = open_nodes.index(next_node)
                    if open_nodes[index][1] > next_node[1]:
                        open_nodes[index] = next_node

    # Retornamos None si no hay ruta
    return None


# Función para calcular la heurística (distancia estimada hasta el destino)
def calculate_heuristic(start_station, destination):
    # Coordenadas de las ciudades
    station_coords = {"X": (0, 0), "Y": (2, 1), "Z": (1, 3), "W": (3, 2), "V": (4, 4), "T": (5, 5)}
    x1, y1 = station_coords[start_station]
    x2, y2 = station_coords[destination]
    # Usamos la distancia de Manhattan como heurística
    return abs(x2 - x1) + abs(y2 - y1)


def optimal_route():
    # Definimos el punto de partida y el destino
    start_station = "X"
    destination = "T"

    # Llamamos a la función para encontrar la mejor ruta
    optimal_route = determine_optimal_route(start_station, destination, knowledge_base)

    # Imprimimos la ruta encontrada
    if optimal_route:
        return (
            "La mejor ruta desde {} hasta {} es:".format(start_station, destination) + "\n" + "->".join(optimal_route)
        )
    else:
        return ("No hay una ruta {} hasta {}".format(start_station, destination))
