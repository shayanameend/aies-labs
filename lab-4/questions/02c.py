graph = {
  'A': ['B', 'D'],
  'B': ['E'],
  'C': ['A'],
  'D': ['G', 'E'],
  'E': ['G'],
  'G': ['F'],
  'F': ['C']
}


def find_all_paths(graph, start, goal, path=None):
  if path is None:
    path = []
  path = path + [start]

  if start == goal:
    return [path]

  if start not in graph:
    return []

  paths = []
  for node in graph[start]:
    if node not in path:
      new_paths = find_all_paths(graph, node, goal, path)
      for p in new_paths:
        paths.append(p)
  return paths


print(find_all_paths(graph, 'A', 'G'))
