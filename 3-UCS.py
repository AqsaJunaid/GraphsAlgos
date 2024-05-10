from queue import PriorityQueue


#***********************  UCS algorithm In PYTHON   ****************************

def uniform_cost_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start]))  # Priority queue with initial cost 0 and start node
    costs = {node: float('inf') for node in graph}  # dictionary that stores the path needed to reach goal
    costs[start] = 0

    while not pq.empty():
        cost, path = pq.get()
        node = path[-1]

        if node not in visited:
            visited.add(node)
            if node == goal:
                return cost, path

            for neighbor, neighbor_cost in graph[node]:
                new_cost = cost + neighbor_cost
                new_path = path + [neighbor]
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    pq.put((new_cost, new_path))

    return None, None #in case of no solution found


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

cost, path = uniform_cost_search(graph, start_node, goal_node)
if path:
    print("Cost from", start_node, "to", goal_node, ":", cost)
    print("Path:", ' -> '.join(path))
else:
    print("No path found from", start_node, "to", goal_node)
