#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, edges):
        '''Solution function description'''
        if not n or not edges: return [0]
        def bfs(stack, dist,  graph):
            while stack:
                #if all([x > 0 for x in dist]): return
                top = stack.pop()
                for n in graph[top]:
                    if dist[n] == -1:
                        dist[n] = dist[top] + 1
                        stack.append(n)
        graph = {}
        for e in edges:
            if e[0] in graph: graph[e[0]].append(e[1])
            else: graph[e[0]] = [e[1]]
            if e[1] in graph: graph[e[1]].append(e[0])
            else: graph[e[1]] = [e[0]]
        res = {}
        for i in range(n):
            dist = [-1] * n
            s = [i]
            dist[i] = 0
            bfs(s, dist, graph)
            d = max(dist)
            if d in res: res[d].append(i)
            else: res[d]=[i]
        return res[min(res)]

def main():
    '''main function'''
    _solution = Solution()
    inp = [(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
