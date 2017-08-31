#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class UndirectedGraphNode:
    '''node class in an undirected graph'''
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    '''Solution description'''
    def cloneGraph(self, node):
        '''Solution function description'''
        if not node: return None
        root = UndirectedGraphNode(node.label)
        d_old_copy = {node: root}
        cur_layer = [node]
        self.bfs(cur_layer, d_old_copy)
        return root
    def bfs(self, cur_layer, d_old_copy):
        '''breadth first'''
        while cur_layer:
            node = cur_layer.pop()
            for nb in node.neighbors:
                if nb not in d_old_copy:
                    d_old_copy[nb] = UndirectedGraphNode(nb.label)
                    #only add unhandled node to stack instead of every neighbor
                    cur_layer.append(nb)
                d_old_copy[node].neighbors.append(d_old_copy[nb])

    def dfs(self, node, d_old_copy):
        '''depth first'''
        for nb in node.neighbors:
            if nb not in d_old_copy:
                d_old_copy[nb] = UndirectedGraphNode(nb.label)
                self.dfs(nb, d_old_copy)
            d_old_copy[node].neighbors.append(d_old_copy[nb])

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.cloneGraph(i))

if __name__ == "__main__":
    main()
