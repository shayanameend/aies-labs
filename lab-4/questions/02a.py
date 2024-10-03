graph = {
  'A': ['B', 'D'],
  'B': ['E'],
  'C': ['A'],
  'D': ['G', 'E'],
  'E': ['G'],
  'G': ['F'],
  'F': ['C']
}


def dfs(graph, start, visited=None):
  if visited is None:
    visited = set()
  visited.add(start)
  print(start)  # This will print the node in the order it is visited.
  for next_node in graph[start]:
    if next_node not in visited:
      dfs(graph, next_node, visited)
  return visited


dfs(graph, 'A')
