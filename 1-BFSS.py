import collections
from collections import deque

#***********************  BFS algorithm In PYTHON   ****************************

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action


def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(vertex, end=" ")  # Print the current node

        # If not visited, mark it as visited, and
        # enqueue its neighbors
        for neighbour in graph[vertex]:
            if neighbour not in visited:
              #n1 = Node(state = chld, parent = vertex, action = act)
               #if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Start Node is 0:")
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
