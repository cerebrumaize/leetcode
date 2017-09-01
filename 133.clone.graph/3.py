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
        if not node: return node
        
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visited = {node.label:root}
        while stack:
            nod = stack.pop()
            for n in nod.neighbors:
                if n.label not in visited:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[nod.label].neighbors.append(visited[n.label])
        
        return root

def main():
    '''main function'''
    _solution = Solution()
    inp = [{0,0,0}]
    for i in inp:
        print(_solution.cloneGraph(i))

if __name__ == "__main__":
    main()
