graph = {
  'A': ['B', 'D'],
  'B': ['E'],
  'C': ['A'],
  'D': ['G', 'E'],
  'E': ['G'],
  'G': ['F'],
  'F': ['C']
}


def find_shortest_path(graph, start, goal):
  from collections import deque
  queue = deque([(start, [start])])  # Stores (current_node, path)

  while queue:
    current, path = queue.popleft()
    for next_node in graph[current]:
      if next_node == goal:
        return path + [next_node]
      elif next_node not in path:
        queue.append((next_node, path + [next_node]))
  return None


print(find_shortest_path(graph, 'A', 'G'))
