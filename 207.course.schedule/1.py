#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, numCourses, prerequisites):
        '''Solution function description'''
        visited = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        def noCircle(v):
            '''depth first search to find whether circle exists'''
            if visited[v] == -1: return False
            if visited[v] == 1: return True
            visited[v] = -1
            for u in graph[v]:
                if not noCircle(u): return False
            visited[v] = 1
            return True

        return all(noCircle(i) for i in range(numCourses))

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
