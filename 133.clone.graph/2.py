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
        if not node:
            return None
        nodecopy = UndirectedGraphNode(node.label)
        dic = {node: nodecopy}
        que = []
        que.append(node)
        #self.dfs(node, dic)
        self.bfs(que, dic)
        
        return nodecopy
        
    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor in dic:
                dic[node].neighbors.append(dic[neighbor])
            else:
                nodecopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = nodecopy
                dic[node].neighbors.append(dic[neighbor])
                self.dfs(neighbor, dic)
    

    def bfs(self, que, dic):
        while len(que) > 0:
            node = que.pop()
            for neighbor in node.neighbors:
                if neighbor in dic:
                    dic[node].neighbors.append(dic[neighbor])
                else:
                    nodecopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = nodecopy
                    dic[node].neighbors.append(dic[neighbor])
                    que.append(neighbor)
            

def main():
    '''main function'''
    _solution = Solution()
    inp = [{0,0,0}]
    for i in inp:
        print(_solution.cloneGraph(i))

if __name__ == "__main__":
    main()
