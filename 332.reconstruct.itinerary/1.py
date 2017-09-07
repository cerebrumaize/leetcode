#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, tickets):
        '''Solution function description'''
        from collections import defaultdict
        graph = defaultdict(list)
        tickets = sorted(tickets, key=lambda x: x[0]+x[1])
        for f, t in tickets:
            graph[f].append(t)
        res = []
        def dfs(source):
            '''solution func dfs'''
            while graph[source]:
                dfs(graph[source].pop())
            res.append(source)
        dfs('JFK')
        return res.sort(reverse=True)
def main():
    '''main function'''
    _solution = Solution()
    inp = [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
