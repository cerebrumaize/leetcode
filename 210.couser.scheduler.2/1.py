#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, numCourses, prerequisites):
        '''Solution function description'''
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        def noCircle(v, res):
            '''depth first searching of circle'''
            if visited[v] == -1:
                return False
            if visited[v] == 1:
                return True
            visited[v] = -1
            for u in graph[v]:
                if not noCircle(u, res): return False
            visited[v] = 1
            res.append(v)
            return True

        res = []
        if all(noCircle(i, res) for i in range(numCourses)): return list(reversed(res))
        else: return []

def main():
    '''main function'''
    _solution = Solution()
    inp = [(4, [[1,0],[2,0],[3,1],[3,2]])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
