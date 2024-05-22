from queue import PriorityQueue

#***********************  DIJISTR'S algorithm In PYTHON   ****************************

def dijkstra(graph, start, goal=None):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))  # Priority queue with initial cost 0 and start node
    costs = {node: float('inf') for node in graph}  # dictionary to store the minimum cost to reach each node
    costs[start] = 0
    predecessors = {node: None for node in graph}  # dictionary to store the path (predecessors)

    while not pq.empty():
        current_cost, current_node = pq.get()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                pq.put((new_cost, neighbor))
                predecessors[neighbor] = current_node

    if goal:
        path = []
        node = goal
        while node:
            path.append(node)
            node = predecessors[node]
        path.reverse()
        return costs[goal], path
    else:
        return costs, predecessors

# Example graph
graph = {
    'A': [['B', 2], ['C', 5]],
    'B': [['D', 4], ['E', 3]],
    'C': [['F', 6]],
    'D': [['G', 7]],
    'E': [['H', 5]],
    'F': [['I', 4]],
    'G': [['J', 6]],
    'H': [['J', 2]],
    'I': [['J', 3]],
    'J': []
}

start_node = 'A'
goal_node = 'J'

cost, path = dijkstra(graph, start_node, goal_node)
if path:
    print("Cost from", start_node, "to", goal_node, ":", cost)
    print("Path:", ' -> '.join(path))
else:
    print("No path found from", start_node, "to", goal_node)
