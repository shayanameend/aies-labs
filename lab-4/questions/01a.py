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


def dfs_traversal(graph, start_node):
  visited = set()
  stack = [start_node]
  traversal = []

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      traversal.append(node)
      for neighbor in reversed(graph.get(node, [])):
        stack.append(neighbor)

  return traversal


dfs_path = dfs_traversal(graph, 1)
print("DFS Traversal:", dfs_path)
