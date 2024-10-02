graph = {
  'A': set(['B', 'C', 'E']),
  'B': set(['D', 'E']),
  'C': set([]),
  'D': set([]),
  'E': set([]),
}


def find_all_paths(graph, start, end, path=None):
  if path is None:
    path = []

  path = path + [start]

  if start == end:
    return [path]

  if start not in graph:
    return []

  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)

  return paths


print(find_all_paths(graph, 'A', 'E'))
