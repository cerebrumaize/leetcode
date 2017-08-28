#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, numCourses, prerequisites):
        '''Solution function description'''
        q = []
        degrees = [0] * numCourses
        from collections import defaultdict
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)
            degrees[p] += 1
        count = 0
        for c, d in enumerate(degrees):
            if d == 0:
                q.append(c)
                count += 1
        while len(q) != 0:
            course = q.pop(0)
            for p in graph[course]:
                degrees[p] -= 1
                if degrees[p] == 0:
                    q.append(p)
                    count += 1
        return count == numCourses

def main():
    '''main function'''
    _solution = Solution()
    inp = [(4, [[0,1],[1,2],[0,2],[1,3]])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
