graph = {
  'A': ['B', 'C', 'E'],
  'B': ['D', 'E'],
  'C': [],
  'D': [],
  'E': [],
}


def dfs(graph, node, visited):
  if node not in visited:
    visited.append(node)

    for neighbour in graph[node]:
      dfs(graph, neighbour, visited)

      return visited


visited = dfs(graph, 'A', [])
print(visited)
