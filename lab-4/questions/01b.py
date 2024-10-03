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


def find_path_dfs(graph, start_node, target_node):
  path = []
  visited = set()

  def dfs(node):
    if node in visited:
      return False
    visited.add(node)
    path.append(node)
    if node == target_node:
      return True
    for neighbor in graph.get(node, []):
      if dfs(neighbor):
        return True
    path.pop()
    return False

  if dfs(start_node):
    return path
  else:
    return None


single_path = find_path_dfs(graph, 1, 6)
print("Single Path from 1 to 6:", single_path)
