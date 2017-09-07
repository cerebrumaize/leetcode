#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, tickets):
        '''Solution function description'''
        from collections import defaultdict
        graph = defaultdict(list)
        tickets.sort(key=lambda x: x[0]+x[1])
        for f, t in tickets:
            graph[f].append(t)
        res, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
