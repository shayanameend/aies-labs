graph = {
  1: [2, 3],
  2: [3, 4],
  3: [4],
  4: [1, 5],
  5: [6, 7],
  6: [7, 8],
  7: [8],
  8: [5]
}


def find_all_paths_dfs(graph, start_node, target_node):
  all_paths = []
  stack = [(start_node, [start_node])]

  while stack:
    (node, path) = stack.pop()
    for neighbor in graph.get(node, []):
      if neighbor not in path:
        if neighbor == target_node:
          all_paths.append(path + [neighbor])
        else:
          stack.append((neighbor, path + [neighbor]))
  return all_paths


all_paths = find_all_paths_dfs(graph, 1, 6)
print("All Paths from 1 to 6:", all_paths)
