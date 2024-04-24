def dfs(graph, start):
  """Performs a Depth-First Search traversal on a graph.

  Args:
      graph: A dictionary representing the graph, where keys are nodes and values are lists of neighbors.
      start: The starting node for the traversal.

  Returns:
      A list containing the nodes visited in the DFS order.
  """
  visited = set()  # Keeps track of visited nodes
  stack = [start]  # Uses a stack for DFS exploration

  while stack:
    current_node = stack.pop()  # Get the last node from the stack
    if current_node not in visited:
      visited.add(current_node)
      stack.extend(graph[current_node])  # Add neighbors to stack for exploration

  return visited

# Example usage (assuming a graph is defined as a dictionary)
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': [],
  'F': []
}

starting_node = 'A'
visited_nodes = dfs(graph, starting_node)

print("DFS traversal from", starting_node, ":", visited_nodes)
