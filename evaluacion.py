import json
from collections import deque

# Aquí estamos simulando la obtención de datos desde una API en formato JSON.
# Estos datos representan las relaciones de seguimiento en una red social ficticia.
datos_json = [
    '{ "user": "userA", "Following": ["userB", "userD", "userE", "userG"] }',
    '{ "user": "userB", "Following": ["userC", "userJ", "userI", "userE"] }',
    '{ "user": "userC", "Following": ["userM", "userN", "userJ", "userI", "userE"] }',
    '{ "user": "userD", "Following": ["userO", "userP"] }',
    '{ "user": "userE", "Following": ["userQ", "userR", "userS"] }',
    '{ "user": "userF", "Following": ["userT", "userU", "userV"] }'
]

# Este bloque de código convierte los datos JSON en un diccionario de Python que representa el grafo de usuarios.
# Cada usuario tiene un conjunto de usuarios a los que sigue, facilitando la búsqueda y navegación entre conexiones.
grafo = {}
for dato in datos_json:
    usuario_info = json.loads(dato)
    grafo[usuario_info["user"]] = set(usuario_info["Following"])

# Función para obtener los usuarios que un usuario específico está siguiendo.

def obtener_seguidos(usuario):
    return grafo.get(usuario, set())

# Implementación de BFS para encontrar la distancia mínima entre dos usuarios en la red social.

def bfs_distancia_minima(inicio, objetivo):
    if inicio == objetivo:
        return 0  # Caso especial: si el inicio y el objetivo son el mismo, no hay distancia.
    cola = deque([(inicio, 0)])  # Cola para BFS, iniciada con el usuario de partida y distancia 0.
    visitados = set([inicio])  # Conjunto para controlar los usuarios ya explorados y evitar ciclos.
    while cola:
        usuario_actual, distancia_actual = cola.popleft()  # Extraemos el usuario y su distancia actual.
        for seguido in obtener_seguidos(usuario_actual):
            if seguido not in visitados:
                if seguido == objetivo:
                    return distancia_actual + 1  # Encontramos el objetivo y retornamos la distancia.
                visitados.add(seguido)  # Marcamos como visitado y continuamos explorando.
                cola.append((seguido, distancia_actual + 1))
    return -1  # Si terminamos de explorar sin encontrar un camino, retornamos -1.

# Ejemplo de uso: Calculando la distancia entre dos usuarios y mostrándola.
usuario_inicio = 'userA'
usuario_objetivo = 'userJ'
distancia = bfs_distancia_minima(usuario_inicio, usuario_objetivo)
print(f"La distancia entre {usuario_inicio} y {usuario_objetivo} es: {distancia}")
