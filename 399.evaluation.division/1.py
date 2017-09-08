#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, equations, values, queries):
        '''Solution function description'''
        from collections import defaultdict
        graph =defaultdict(list)
        weights = defaultdict(float)
        for i, e in enumerate(equations):
            graph[e[0]].append(e[1])
            if values[i]!=0: graph[e[1]].append(e[0])
            weights[(e[0], e[1])]=(values[i])
            if values[i]!=0: weights[(e[1], e[0])]=(1/values[i])
        res = []
        def dfs(source, target, bu):
            while bu[source]:
                x = bu[source].pop()
                bu[x].remove(source)
                if x == target:
                    return weights[(source, x)]
                else:
                    t = dfs(x, target, bu)
                    if t is -1: continue
                    else:
                        return weights[(source, x)]*t
            return -1
        from copy import deepcopy
        for q in queries:
            if q[0] in graph and q[0] == q[1]: res.append(1.0)
            elif (q[0], q[1]) in weights: res.append(weights[(q[0], q[1])])
            else:
                bu = deepcopy(graph)
                t = dfs(q[0], q[1], bu)
                res.append(t)
        return res


def main():
    '''main function'''
    _solution = Solution()
    inp = [([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]), 
           ([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]),
           ([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],[3.0,0.5,3.4,5.6],[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]])]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()
