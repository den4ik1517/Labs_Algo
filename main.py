from collections import deque

def read_adjacency_list(file_path):
    with open(file_path, 'r') as file:
        graph = {}
        for line in file:
            try:
                vertex, edges = line.strip().split(':')
            except ValueError:
                continue

            edges = [e.strip() for e in edges.split()]
            graph[vertex] = edges
    return graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([u for u in graph[vertex] if u not in visited])

    return visited

def find_roots(graph):
    all_vertices = set(graph.keys())
    for edges in graph.values():
        for edge in edges:
            if edge not in graph:
                graph[edge] = []

    for vertex in all_vertices:
        if bfs(graph, vertex) == all_vertices:
            return [vertex]

    return []

file_path = 'input.txt'
graph = read_adjacency_list(file_path)

root_vertices = find_roots(graph)

with open('output.txt', 'w') as f:
    if root_vertices:
        for root in root_vertices:
            f.write(f'{root}\n')
    else:
        f.write('-1\n')

if root_vertices:
    print(f'Root vertices: {root_vertices}')
else:
    print('No root vertices found. Written -1 to output.txt')
