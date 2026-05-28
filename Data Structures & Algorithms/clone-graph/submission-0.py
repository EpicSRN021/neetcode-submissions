"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        if node == None:
            return None
        queue = deque()
        queue.append(node)
        visited[node.val] = Node(node.val)
        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n.val not in visited:
                    queue.append(n)
                    visited[n.val] = Node(n.val)
                visited[curr.val].neighbors.append(visited[n.val])

        return visited[node.val]
            
