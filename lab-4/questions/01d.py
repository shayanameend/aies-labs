from collections import deque

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


def find_shortest_path_bfs(graph, start_node, target_node):
  queue = deque([(start_node, [start_node])])
  visited = set()

  while queue:
    (node, path) = queue.popleft()
    if node in visited:
      continue
    visited.add(node)
    for neighbor in graph.get(node, []):
      if neighbor == target_node:
        return path + [neighbor]
      else:
        queue.append((neighbor, path + [neighbor]))
  return None


shortest_path = find_shortest_path_bfs(graph, 1, 6)
print("Shortest Path from 1 to 6:", shortest_path)
