#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, edges):
        '''Solution function description'''
        graph=[set() for _ in range(n)]
        for u,v in edges: 
            graph[u].add(v)
            graph[v].add(u)
        q = [i for i in range(n) if len(graph[i])==1]
        while n>2:
            n -= len(q)
            newq = []
            for i in q:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1: newq.append(j)
            q = newq
        return q

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
