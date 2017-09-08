#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, equations, values, queries):
        '''Solution function description'''
        from collections import deque
        graph = {}
        for i, e in enumerate(equations):
            v = values[i]
            if e[0] not in graph: graph[e[0]]=[]
            graph[e[0]].append((e[1], v))
            if e[1] not in graph: graph[e[1]]=[]
            graph[e[1]].append((e[0], 1.0/v))
        res = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph: res.append(-1.0)
            elif q[0]==q[1]: res.append(1.0)
            else:
                queue = deque([(q[0], 1.0)])
                visited = set([q[0]])
                found = False
                while queue and not found:
                    node, value = queue.popleft()
                    for n, v in graph[node]:
                        if n == q[1]: res.append(value*v)
                        elif n not in visited:
                            queue.append((n, value*v))
                            visited.add(n)
                if not found: res.append(-1.0)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    inp = [([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]), 
           ([["x1","x2"], ["x2","x3"], ["x3","x4"], ["x4","x5"]], [ 3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]),
           ([["x1","x2"], ["x2","x3"], ["x1","x4"], ["x2","x5"]], [ 3.0,0.5,3.4,5.6],[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]])]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()
