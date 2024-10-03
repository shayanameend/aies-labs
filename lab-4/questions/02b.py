graph = {
  'A': ['B', 'D'],
  'B': ['E'],
  'C': ['A'],
  'D': ['G', 'E'],
  'E': ['G'],
  'G': ['F'],
  'F': ['C']
}


def dfs_find_path(graph, start, goal, path=None):
  if path is None:
    path = []
  path.append(start)

  if start == goal:
    return path

  for next_node in graph[start]:
    if next_node not in path:
      result = dfs_find_path(graph, next_node, goal, path.copy())
      if result:
        return result
  return None


print(dfs_find_path(graph, 'A', 'G'))
