import collections

#***********************  DFS algorithm In PYTHON   ****************************
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


def dfs(graph, root):
    visited, stack = set(), [root]
    visited.add(root)

    while stack:
        # Pop a vertex from stack
        vertex = stack.pop() 

        # If not visited, mark it as visited
        # and push its neighbors onto the stack
        for neighbour in graph[vertex.state]:
            n1 = Node(state=neighbour, parent=vertex, action=None)
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(n1)
                
    print(vertex.state, end=" ") 

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Depth First Traversal: ")
    n = Node(state=0, parent=None, action=None)
    dfs(graph, n)
