#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class UndirectedGraphNode:
    '''Class UndirectedGraphNode description'''
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    '''
    @param node, a undirected graph node
    @return a undirected graph node
    '''
    def cloneGraph(self, node):
        if not node: return None
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visited = {}
        visited[node.label] = root
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in visited.keys:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[n.label].neighbors.append(visited[n.label])

        return root

def main():
    '''main function'''
    _solution = Solution()
    inp = [{0,0,0}]
    for i in inp:
        print(_solution.cloneGraph(i))

if __name__ == "__main__":
    main()
