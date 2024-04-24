def bfs(graph, start):
  """Performs a Breadth-First Search traversal on a graph.

  Args:
      graph: A dictionary representing the graph, where keys are nodes and values are lists of neighbors.
      start: The starting node for the traversal.

  Returns:
      A list containing the nodes visited in the BFS order.
  """
  visited = set()  # Keeps track of visited nodes
  queue = [start]  # Uses a queue for BFS exploration

  while queue:
    current_node = queue.pop(0)  # Get the first node from the queue
    if current_node not in visited:
      visited.add(current_node)
      queue.extend(graph[current_node])  # Add neighbors to queue for exploration

  return visited

# Define an example graph as a dictionary
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': [],
  'F': []
}

# Starting node for traversal
starting_node = 'A'

# Perform BFS traversal and print visited nodes
visited_nodes = bfs(graph, starting_node)
print("BFS traversal from", starting_node, ":", visited_nodes)
